from typing import Annotated

from fastapi import APIRouter, Body
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
            body: Annotated[RequestValidation, Body(..., description="Message request body")],
    ) -> list[TextBlock]:
        """
        Create message using Anthropic.

        Args:
            body (RequestValidation): Message request body.

        Returns:
            response: Message response.
        """
        response = await AnthropicService.create_message(body)
        return response.content

    @staticmethod
    @router.post(
        path='/message/detailed',
        summary="Create Message using Anthropic (Detailed)",
        response_model_by_alias=True,
        tags=tags,
    )
    async def create_message_detailed(
            body: Annotated[RequestValidation, Body(..., description="Message request body")],
    ) -> ResponseValidation:
        """
        Create message using Anthropic. Detailed response.

        Args:
            body (RequestValidation): Message request body.

        Returns:
            response: Message response.
        """
        return await AnthropicService.create_message(body)

    @staticmethod
    @router.post(
        path='/stream',
        summary="Stream Message using Anthropic",
        response_model_by_alias=True,
        tags=tags,
    )
    async def create_stream(
            body: Annotated[RequestValidation, Body(..., description="Message request body")],
    ) -> StreamingResponse:
        """
        Stream message using Anthropic.

        Args:
            body (RequestValidation): Message request body.

        Returns:
            response: Message response.
        """
        return await AnthropicService.create_stream(body)
