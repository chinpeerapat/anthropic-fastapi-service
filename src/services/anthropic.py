from fastapi.responses import StreamingResponse

from src.configs import BusinessLogicConfig
from src.errors import ServiceError
from src.utils.anthropic import anthropic_client
from src.validations import ResponseValidation, RequestValidation


class AnthropicService:

    @staticmethod
    async def create_message(request: RequestValidation) -> ResponseValidation:
        """
        Create message on anthropic.

        Args:
            request (RequestValidation): Anthropic request validation.

        Returns:
            MessageResponseValidation: Anthropic Message response.
        """
        system = BusinessLogicConfig.get_system_message(system=request.system)

        try:
            return await anthropic_client.create_message(messages=request.messages, system=system, model=request.model,
                                                         max_tokens=request.max_tokens, temperature=request.temperature)
        except Exception as e:
            raise ServiceError(f"Failed to create message on anthropic: {str(e)}")

    @staticmethod
    async def create_stream(request: RequestValidation) -> StreamingResponse:
        """
        Create stream message on anthropic.

        Args:
            request (RequestValidation): Anthropic request validation.

        Returns:
            StreamingResponse: Anthropic Message response.
        """
        system = BusinessLogicConfig.get_system_message(system=request.system)

        try:
            return StreamingResponse(
                content=anthropic_client.create_stream(messages=request.messages, system=system,
                                                       model=request.model,
                                                       max_tokens=request.max_tokens,
                                                       temperature=request.temperature),
                media_type="text/plain")
        except Exception as e:
            raise ServiceError(f"Failed to create stream message on anthropic: {str(e)}")
