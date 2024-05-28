from .router import Router
from src.controllers import AnthropicController

anthropic_route = Router(router=AnthropicController.router)

__all__ = [
    "anthropic_route",
]
