import json

from pydantic import BaseModel, Field, model_validator
from .message import MessageRequestValidation, MessageResponseValidation
from ..constants import AnthropicConstant


class RequestValidation(BaseModel):
    messages: list[MessageRequestValidation]
    system: str | None = Field("You are a personal AI assistant",
                               title='System', description='The system name.')
    max_tokens: int | None = Field(1024, ge=1, title='Max Tokens',
                                   description='The maximum number of tokens to generate.')
    temperature: float | None = Field(0.8, title='Temperature', gt=0.0, le=1.0,
                                      description='The sampling temperature.')
    model: AnthropicConstant.Model | None = Field(AnthropicConstant.Model.CLAUDE_3_OPUS_20240229,
                                                  title='Model', description='The model name.')

    @model_validator(mode="before")
    @classmethod
    def to_py_dict(cls, data):
        return json.loads(data)


class ResponseValidation(MessageResponseValidation):
    pass
