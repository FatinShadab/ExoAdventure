from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router import ROUTERS
from .settings.middleware import cors_settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    **cors_settings
)

[
    app.include_router(router) for router in ROUTERS
]
