import os
from .core import FRONTEND_URL

origins = [FRONTEND_URL]

cors_settings = {
    "allow_origins": origins,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}