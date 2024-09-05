"""
firebase.py

Setup and initialize Firebase with FastAPI integration.
"""

from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import initialize_app, credentials, App
from .core import FIREBASE_CREDENTIALS_PATH, FIREBASE_DB_URL

# Initialize Firebase credentials
FIREBASE_CREDENTIALS: credentials.Certificate = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)

# Raise HTTPException if FIREBASE_DB_URL is not set
if not FIREBASE_DB_URL:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='FIREBASE_DB_URL env variable is not set!'
    )

# Initialize Firebase app with credentials and database URL
FIREBASE_APP: App = initialize_app(FIREBASE_CREDENTIALS, {
    'databaseURL': FIREBASE_DB_URL
})

# Define HTTPBearer for security
FIREBASE_BEARER: HTTPBearer = HTTPBearer(auto_error=False)
