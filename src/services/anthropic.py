from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import UploadFile
from fastapi.responses import StreamingResponse

from src.configs import BusinessLogicConfig
from src.constants import AnthropicConstant
from src.errors import ServiceError
from src.utils.anthropic import anthropic_client
from src.validations import ResponseValidation, RequestValidation
from src.validations.message import ImageSource, TextBlock, ImageBlock


class AnthropicService:

    @staticmethod
    async def create_message(body: RequestValidation, files: list[UploadFile]) -> ResponseValidation:
        """
        Create message on anthropic.

        Args:
            body (RequestValidation): Anthropic request validation.
            files (list[UploadFile]): Image translation files.

        Returns:
            MessageResponseValidation: Anthropic Message response.
        """
        if files and len(files) > 0:
            if len(body.messages) != 1:
                raise ServiceError("Only one message is allowed when uploading files.")

            content = body.messages[0].content
            text = content if isinstance(content, str) else next(iter(content), None).text
            body.messages[0].content = [TextBlock(text=text, type=AnthropicConstant.TextBlock.Type.TEXT)]

        for file in files:
            if file.content_type not in [AnthropicConstant.ImageBlock.MediaType.JPEG,
                                         AnthropicConstant.ImageBlock.MediaType.PNG,
                                         AnthropicConstant.ImageBlock.MediaType.GIF,
                                         AnthropicConstant.ImageBlock.MediaType.WEBP]:
                raise ServiceError(f"Invalid file type: {file.content_type}")

            # Save data to temporary file
            temp_file = NamedTemporaryFile(delete=True, suffix=file.filename)
            temp_file.write(file.file.read())

            image_source = ImageSource(media_type=file.content_type,
                                       type=AnthropicConstant.ImageBlock.DataFormat.BASE64,
                                       data=Path(temp_file.name))

            image_block = ImageBlock(source=image_source, type=AnthropicConstant.ImageBlock.Type.IMAGE)
            body.messages[0].content.append(image_block)

        system = BusinessLogicConfig.get_system_message(system=body.system)

        try:
            return await anthropic_client.create_message(messages=body.messages, system=system, model=body.model,
                                                         max_tokens=body.max_tokens, temperature=body.temperature)
        except Exception as e:
            raise ServiceError(f"Failed to create message on anthropic: {str(e)}")

    @staticmethod
    async def create_stream(body: RequestValidation) -> StreamingResponse:
        """
        Create stream message on anthropic.

        Args:
            body (RequestValidation): Anthropic request validation.

        Returns:
            StreamingResponse: Anthropic Message response.
        """
        system = BusinessLogicConfig.get_system_message(system=body.system)

        try:
            return StreamingResponse(
                content=anthropic_client.create_stream(messages=body.messages, system=system,
                                                       model=body.model,
                                                       max_tokens=body.max_tokens,
                                                       temperature=body.temperature),
                media_type="text/plain")
        except Exception as e:
            raise ServiceError(f"Failed to create stream message on anthropic: {str(e)}")
