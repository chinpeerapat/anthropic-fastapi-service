from typing import Annotated, Optional

from fastapi import APIRouter, UploadFile, File, Form, Body
from fastapi.responses import StreamingResponse

from src.services import AnthropicService
from src.validations import RequestValidation, ResponseValidation
from src.validations.message import TextBlock


class AnthropicController:
    router = APIRouter()

    tags = ['Anthropic']

    @staticmethod
    @router.post(
        path='/message',
        summary="Create Message using Anthropic",
        response_model_by_alias=True,
        response_model=list[TextBlock],
        tags=tags,
    )
    async def create_message(
            body: Annotated[RequestValidation, Form(..., description="Message request body")],
    ) -> list[TextBlock]:
        """
        Create message using Anthropic.

        Args:
            body (RequestValidation): Message request body.

        Returns:
            response: Message response.
        """
        response = await AnthropicService.create_message(body, [])
        return response.content

    @staticmethod
    @router.post(
        path='/message/detailed',
        summary="Create Message using Anthropic (Detailed)",
        response_model_by_alias=True,
        tags=tags,
    )
    async def create_message_detailed(
            body: Annotated[RequestValidation, Form(..., description="Message request body")],
    ) -> ResponseValidation:
        """
        Create message using Anthropic. Detailed response.

        Args:
            body (RequestValidation): Message request body.

        Returns:
            response: Message response.
        """
        return await AnthropicService.create_message(body, [])

    @staticmethod
    @router.post(
        path='/stream',
        summary="Stream Message using Anthropic",
        response_model_by_alias=True,
        tags=tags,
    )
    async def create_stream(
            body: Annotated[RequestValidation, Form(..., description="Message request body")],
    ) -> StreamingResponse:
        """
        Stream message using Anthropic.

        Args:
            body (RequestValidation): Message request body.
            files (list[UploadFile]): Image translation files.

        Returns:
            response: Message response.
        """
        return await AnthropicService.create_stream(body)

    @staticmethod
    @router.post(
        path='/upload',
        summary="Upload Files to Anthropic",
        response_model_by_alias=True,
        tags=tags,
    )
    async def upload_files(
            body: Annotated[RequestValidation, Form(..., description="Message request body")],
            files: Annotated[list[UploadFile], File(description="Image translation files")],
    ) -> ResponseValidation:
        """
        Upload files to Anthropic.

        Args:
            body (RequestValidation): Message request body.
            files (list[UploadFile]): Image translation files.

        Returns:
            response: Message response.
        """
        return await AnthropicService.create_message(body, files)

    @staticmethod
    @router.post(
        path='/upload/detailed',
        summary="Upload Files to Anthropic (Detailed)",
        response_model_by_alias=True,
        tags=tags,
    )
    async def upload_files_detailed(
            body: Annotated[RequestValidation, Form(..., description="Message request body")],
            files: Annotated[list[UploadFile], File(description="Image translation files")],
    ) -> ResponseValidation:
        """
        Upload files to Anthropic. Detailed response.

        Args:
            body (RequestValidation): Message request body.
            files (list[UploadFile]): Image translation files.

        Returns:
            response: Message response.
        """
        return await AnthropicService.create_message(body, files)
