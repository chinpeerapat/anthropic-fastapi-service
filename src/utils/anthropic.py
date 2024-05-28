from anthropic import AsyncAnthropic
from src.configs import ServiceCallerConfig
from src.constants import AnthropicConstant
from src.validations import MessageResponseValidation, MessageRequestValidation

from src.errors import ServiceError


class AnthropicClient:
    def __init__(self):
        """
        Initialize Anthropic service.
        """
        anthropic_api_key = ServiceCallerConfig.Anthropic.API_KEY
        if not anthropic_api_key:
            raise ServiceError("Anthropic API key is not set.")

        self.anthropic = AsyncAnthropic(api_key=anthropic_api_key)

    async def create_message(self, messages: [MessageRequestValidation], system: str,
                             max_tokens: int = ServiceCallerConfig.Anthropic.MAX_TOKEN,
                             temperature: float = ServiceCallerConfig.Anthropic.TEMPERATURE,
                             model: AnthropicConstant.Model = ServiceCallerConfig.Anthropic.MODEL) \
            -> MessageResponseValidation:
        """
        Create async message on anthropic.

        Args:
            messages (list): Messages to send.
            system (str): System message.
            max_tokens (int): Maximum tokens.
            temperature (float): Temperature.
            model (str): Model name.

        Returns:
            MessageResponseValidation: Anthropic Message response.
        """
        max_tokens = max_tokens or ServiceCallerConfig.Anthropic.MAX_TOKEN
        temperature = temperature or ServiceCallerConfig.Anthropic.TEMPERATURE
        model = model or ServiceCallerConfig.Anthropic.MODEL
        message = await self.anthropic.messages.create(model=model, max_tokens=max_tokens, temperature=temperature,
                                                       system=system, messages=messages)
        return MessageResponseValidation(**message.model_dump())

    async def create_stream(self, messages: [MessageRequestValidation], system: str,
                            max_tokens: int = ServiceCallerConfig.Anthropic.MAX_TOKEN,
                            temperature: float = ServiceCallerConfig.Anthropic.TEMPERATURE,
                            model: AnthropicConstant.Model = ServiceCallerConfig.Anthropic.MODEL):
        """
        Create stream message on anthropic.

        Args:
            messages (list): Messages to send.
            system (str): System description.
            max_tokens (int): Maximum tokens.
            temperature (float): Temperature.
            model (str): Model name.

        Returns:
            MessageResponseValidation: Anthropic Message response.
        """
        async with self.anthropic.messages.stream(model=model, max_tokens=max_tokens, temperature=temperature,
                                                  system=system, messages=messages) as stream:
            async for text in stream.text_stream:
                yield text


anthropic_client = AnthropicClient()
