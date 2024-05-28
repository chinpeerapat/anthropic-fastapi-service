from dotenv import load_dotenv
from os import environ as env

load_dotenv()

DEBUG = env.get('DEBUG', 'False').lower() in ('true', '1', 't')
URL = env.get('DEVELOPMENT_URL', 'http://127.0.0.1:8000') if DEBUG else env.get('PRODUCTION_URL', None)


class AppConfig:
    DEBUG: bool = DEBUG
    TESTING: bool = env.get('TESTING', 'False').lower() in ('true', '1', 't')

    NAME: str = env.get('NAME', 'anthropic-fastapi')
    DESCRIPTION: str = env.get('DESCRIPTION', 'Anthropic FastAPI Service')
    VERSION: str = env.get('VERSION', '1.0.0')

