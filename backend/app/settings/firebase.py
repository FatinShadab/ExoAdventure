"""
firebase.py

Setup and initialize Firebase with FastAPI integration.
"""
import json
import pyrebase
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer
from firebase_admin import initialize_app, credentials, App
from .core import (
    FIREBASE_CREDENTIALS_PATH, FIREBASE_DB_URL,
    FIRE_STORE_ENABLE, FIREBASE_RTDB_ENABLE,
    PYREBASE_CREDENTIALS_PATH
)

# Initialize Firebase credentials
FIREBASE_CREDENTIALS: credentials.Certificate = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)

# Raise HTTPException if FIREBASE_DB_URL is not set
if not FIREBASE_DB_URL and FIREBASE_RTDB_ENABLE:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='FIREBASE_DB_URL env variable is not set!'
    )

# Initialize Firebase app with credentials and database URL
FIREBASE_APP: App = initialize_app(FIREBASE_CREDENTIALS, {
    'databaseURL': FIREBASE_DB_URL
})


if FIREBASE_RTDB_ENABLE:
    from firebase_admin import db
    # Define Firebase database reference
    FIREBASE_RTDB: db.Reference = db.reference()  # Firebase database reference

if FIRE_STORE_ENABLE:
    # Initialize Firestore
    from firebase_admin import firestore
    FIRESTORE: firestore.Client = firestore.client()  # Firestore client

# Define HTTPBearer for security
FIREBASE_BEARER: HTTPBearer = HTTPBearer(auto_error=False)


if PYREBASE_CREDENTIALS_PATH:
    # Read the Firebase credentials JSON file and convert it to a Python dictionary
    with open(PYREBASE_CREDENTIALS_PATH, 'r') as f:
        firebase_credentials = json.load(f)
    
    # Initialize Pyrebase app with the credentials
    PYREBASE_APP: pyrebase.pyrebase.Firebase = pyrebase.initialize_app(firebase_credentials)