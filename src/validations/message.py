# This file is taken from the Claude API documentation and is used to validate the request and response of the message

from os import PathLike
from typing import Iterable, Annotated

from pydantic import BaseModel

from src.constants import AnthropicConstant


class Usage(BaseModel):
    input_tokens: int
    output_tokens: int


class ImageSource(BaseModel):
    media_type: AnthropicConstant.ImageBlock.MediaType
    type: AnthropicConstant.ImageBlock.DataFormat
    data: Annotated[str | PathLike, dict(format=AnthropicConstant.ImageBlock.DataFormat.BASE64)]


class TextBlock(BaseModel):
    text: str
    type: AnthropicConstant.TextBlock.Type


class ImageBlock(BaseModel):
    source: ImageSource
    type: AnthropicConstant.ImageBlock.Type


class MessageRequestValidation(BaseModel):
    content: str | Iterable[TextBlock | ImageBlock]
    role: AnthropicConstant.Role


class MessageResponseValidation(BaseModel):
    id: str
    content: list[TextBlock]
    role: AnthropicConstant.Role
    model: str
    stop_reason: AnthropicConstant.StopReason | None = None
    stop_sequence: str | None = None
    type: AnthropicConstant.Type
    usage: Usage
