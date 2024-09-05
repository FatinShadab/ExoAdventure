"""
core.py

Configuration and environment setup for the application. 
Loads environment variables and handles defaults and warnings.
"""

import os
import pathlib
import warnings
from dotenv import load_dotenv

# Base directory of the project
BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent.parent

# Path to the .env file
ENV_PATH: pathlib.Path = BASE_DIR / '.env'

load_dotenv()  # Load environment variables from .env file

# Application name
APP_NAME: str = 'app'

# Default frontend URL
DEFAULT_FRONTEND_URL: str = 'http://localhost:3000'

# Application environment (default: 'development')
ENV: str = os.getenv('ENV', 'development')

# Frontend URL (defaults to DEFAULT_FRONTEND_URL if not set)
FRONTEND_URL: str = os.getenv('FRONTEND_URL', DEFAULT_FRONTEND_URL)

# Warning if FRONTEND_URL is not set
if FRONTEND_URL == DEFAULT_FRONTEND_URL:
    warnings.warn(f'FRONTEND_URL env variable is not set! Using default value: {DEFAULT_FRONTEND_URL}')

# Firebase application identifier (None if not set)
FIREBASE_APP: str | None = os.getenv('FIREBASE_APP', None)

if FIREBASE_APP:
    print('INFO: FIREBASE_APP env variable FOUND!')

    # Firebase credentials filename
    FIREBASE_CREDENTIALS_FNAME: str = os.getenv('FIREBASE_CREDENTIALS_FNAME', '')

    # Warning if FIREBASE_CREDENTIALS_FNAME is not set
    if not FIREBASE_CREDENTIALS_FNAME:
        warnings.warn('FIREBASE_CREDENTIALS_FNAME env variable is not set!')

    # Path to the Firebase credentials file
    FIREBASE_CREDENTIALS_PATH: pathlib.Path = BASE_DIR / FIREBASE_CREDENTIALS_FNAME

    # Firebase database URL (None if not set)
    FIREBASE_DB_URL: str | None = os.getenv('FIREBASE_DB_URL', None)

    # Warning if FIREBASE_DB_URL is not set
    if not FIREBASE_DB_URL:
        warnings.warn('FIREBASE_DB_URL env variable is not set!')
