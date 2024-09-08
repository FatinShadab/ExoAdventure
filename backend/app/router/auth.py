"""
auth.py

This module defines API routes related to authentication using FastAPI.

Endpoints:
- `/signin`: Handles user sign-in with email and password.
- `/signup`: Handles user sign-up with email and password.
- `/signout`: Handles user sign-out (client-side operation).
- `/ping`: Verifies the provided token and returns user information.
- `/validate`: Validates the authorization token using middleware.

Dependencies:
- `verify_token`: Middleware function to verify the validity of an authorization token.

Schemas:
- `SignInSchema`: Schema for user sign-in information (email and password).
- `SignUpSchema`: Schema for user sign-up information (email and password).
- `TokenSchema`: Schema for token verification (access token).

Controllers:
- `signin_controller`: Handles the sign-in process.
- `signup_controller`: Handles the sign-up process.
- `signout_controller`: Handles the sign-out process.
- `ping_controller`: Verifies the token and returns user information.
"""

from fastapi import APIRouter, Depends
from app.middleware.token_validation import verify_token
from app.schema.auth import SignInSchema, SignUpSchema, TokenSchema
from app.controller.auth_contoller import (
    signin_controller, signup_controller,
    signout_controller, ping_controller
)

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signin")
async def signin(data: SignInSchema):
    """
    Sign in a user with email and password.

    Args:
        data (SignInSchema): User sign-in information.

    Returns:
        dict: Response including access token and status information.
    """
    return await signin_controller(data)

@router.post("/signup")
async def signup(data: SignUpSchema):
    """
    Sign up a new user with email and password.

    Args:
        data (SignUpSchema): User sign-up information.

    Returns:
        dict: Response including access token and status information.
    """
    return await signup_controller(data)

@router.post("/signout")
async def signout():
    """
    Sign out the current user.

    Returns:
        dict: Response confirming sign-out status.
    """
    return await signout_controller()

@router.post("/ping")
async def ping(data: TokenSchema):
    """
    Verify the provided access token and return user information.

    Args:
        data (TokenSchema): Token information.

    Returns:
        dict: Response including user information and status.
    """
    return await ping_controller(data)

@router.post("/validate")
async def validate(decoded_token=Depends(verify_token)):
    """
    Validate the authorization token using middleware.

    Args:
        decoded_token (dict): Decoded token information from middleware.

    Returns:
        dict: Response confirming token validity and user ID.
    """
    return {"status": "success", "status_code": 200, "uid": decoded_token["uid"], "msg": "Token is valid."}
