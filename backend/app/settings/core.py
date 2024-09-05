import os
import pathlib
import warnings
from dotenv import load_dotenv

BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent.parent

ENV_PATH: pathlib.Path = BASE_DIR / '.env'

load_dotenv()

APP_NAME: str = 'app'
DEFAULT_FORNTEND_URL: str = 'http://localhost:3000'

ENV: str = os.getenv('ENV', 'development')

FRONTEND_URL: str = os.getenv('FRONTEND_URL', DEFAULT_FORNTEND_URL)

if FRONTEND_URL == DEFAULT_FORNTEND_URL:
    warnings.warn(f'FRONTEND_URL env variable is not set ! Using default value: {DEFAULT_FORNTEND_URL}')

FIREBASE_APP: str | None = os.getenv('FIREBASE_APP', None)

if FIREBASE_APP:
    print('INFO: \t  FIREBASE_APP env variable FOUND !')

    FIREBASE_CREDENTIALS_FNAME: str = os.getenv('FIREBASE_CREDENTIALS_FNAME', '')

    if not FIREBASE_CREDENTIALS_FNAME:
        warnings.warn('FIREBASE_CREDENTIALS_FNAME env variable is not set !')

    FIREBASE_CREDENTIALS_PATH: pathlib.Path = BASE_DIR / FIREBASE_CREDENTIALS_FNAME

    FIREBASE_DB_URL: str | None = os.getenv('FIREBASE_DB_URL', None)

    if not FIREBASE_DB_URL:
        warnings.warn('FIREBASE_DB_URL env variable is not set !')