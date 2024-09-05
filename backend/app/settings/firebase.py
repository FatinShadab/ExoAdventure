from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from firebase_admin import initialize_app, credentials

from .core import FIREBASE_CREDENTIALS_PATH
from .core import FIREBASE_DB_URL


FIREBASE_CREDENTIALS = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)

if not FIREBASE_DB_URL:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='FIREBASE_DB_URL env variable is not set !'
    )

FIREBASE_APP = initialize_app(FIREBASE_CREDENTIALS, {
    'databaseURL': FIREBASE_DB_URL
})

FIREBASE_BAREAR = HTTPBearer(auto_error=False)