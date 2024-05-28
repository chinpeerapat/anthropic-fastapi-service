from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.utils.http import http_client
from src.errors import ValidationError, HTTPError

from src.configs import AppConfig
from . import routers

app = FastAPI(
    debug=AppConfig.DEBUG,
    title=AppConfig.NAME,
    description=AppConfig.DESCRIPTION,
    version=AppConfig.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Re-raise so we can handle in exception middleware
    raise ValidationError("Pydantic Validation Error", detail=exc.errors(), caught_exception=exc)


@app.exception_handler(HTTPError)
async def http_exception_handler(request: Request, exc: HTTPError):
    if AppConfig.TESTING:
        raise exc.caught_exception
    return JSONResponse(exc.dict(), status_code=exc.status_code)


@app.on_event("startup")
async def startup():
    await http_client.start()


@app.on_event("shutdown")
async def shutdown():
    await http_client.stop()


for router in routers.__all__:
    app.include_router(**getattr(routers, router).__dict__)


@app.get("/")
def index():
    return f"{AppConfig.NAME} v{AppConfig.VERSION}"


@app.get("/health")
async def health():
    return {"message": "healthy"}
