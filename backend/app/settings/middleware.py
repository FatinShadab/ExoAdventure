"""
middleware.py

CORS settings for FastAPI to handle cross-origin requests.
"""
from typing import List, Dict, Union
from .core import FRONTEND_URL

# List of allowed origins
origins: List[str] = [FRONTEND_URL]

# CORS settings configuration
cors_settings: Dict[str, Union[List[str], bool]] = {
    "allow_origins": origins,        # Allow requests from these origins
    "allow_credentials": True,       # Allow cookies and authentication
    "allow_methods": ["*"],          # Allow all HTTP methods
    "allow_headers": ["*"],          # Allow all headers
}
