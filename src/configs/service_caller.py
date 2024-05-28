import os


class ServiceCallerConfig:
    class Anthropic:
        API_KEY: str = os.environ.get('ANTHROPIC_API_KEY')
        MODEL: str = os.environ.get('GPT_MODEL', 'claude-3-opus-20240229')
        MAX_TOKEN: str = os.environ.get('MAX_TOKEN', 1024)
        TEMPERATURE: str = os.environ.get('TEMPERATURE', 0.8)
