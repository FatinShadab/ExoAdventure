"""
token_validation.py

This module contains middleware functions to handle token validation using Firebase Admin SDK.
It ensures that each incoming request has a valid Firebase authentication token.

Functions:
    - verify_token(request: Request): Verifies the Bearer token from the request headers 
      and decodes it using Firebase Admin. Raises an HTTPException if the token is invalid 
      or missing.

Usage:
    Add this middleware function to your FastAPI route handlers to ensure that incoming requests 
    are authenticated using Firebase tokens.

Dependencies:
    - fastapi.Request: To access request data.
    - fastapi.HTTPException: To handle HTTP errors when authentication fails.
    - firebase_admin.auth: For verifying Firebase ID tokens.
    - firebase_admin.exceptions: To catch errors from Firebase Admin SDK during token verification.
"""

from fastapi import Request, HTTPException
from firebase_admin import auth, exceptions

async def verify_token(request: Request):
    """
    Verifies the Firebase Bearer token from the Authorization header of the incoming request.
    
    Args:
        request (Request): The incoming HTTP request object.
    
    Returns:
        dict: The decoded Firebase token if verification is successful.
    
    Raises:
        HTTPException: If the Authorization header is missing, the token is invalid, 
        or any error occurs during Firebase token verification.
    """
    
    # Get the Authorization header from the request
    authorization: str = request.headers.get("Authorization")

    # Raise an error if the Authorization header is missing or does not start with "Bearer"
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Authorization token missing or invalid")

    # Extract the token from the header
    token = authorization.split(" ")[1]

    try:
        # Verify and decode the Firebase token
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except exceptions.FirebaseError as e:
        # Raise an error if the token is invalid or verification fails
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")
