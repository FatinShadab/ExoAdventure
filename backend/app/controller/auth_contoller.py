"""
    auth_controller.py

    This module provides controller functions for handling user authentication actions using Pyrebase.

    Functions:
    - signin_controller(data: SignInSchema) -> dict: Handles user sign-in by verifying the provided email and password. Returns an access token and token type upon successful authentication or an error message if authentication fails.
    - signup_controller(data: SignUpSchema) -> dict: Handles user sign-up by creating a new user with the provided email and password. Returns an access token and token type upon successful registration or an error message if registration fails.
    - signout_controller() -> dict: Handles user sign-out. Note that sign-out is generally managed on the client side, so this function sets the current user to None as a placeholder.
    - ping_controller(data: TokenSchema) -> dict: Verifies the provided access token using Pyrebase and returns user information if the token is valid. Returns an error message if the token is invalid.

    Dependencies:
    - Pyrebase: For interacting with Firebase Authentication services.
    - Schema: For data validation of user credentials and tokens.
"""

from app.settings.firebase import PYREBASE_APP as AUTH_PROVIDER
from app.schema.auth import SignInSchema, SignUpSchema, TokenSchema

async def signin_controller(data: SignInSchema) -> dict:
    """
    Handle user sign-in by verifying email and password with Pyrebase.

    Args:
        data (SignInSchema): The sign-in data containing email and password.

    Returns:
        dict: A dictionary containing the status of the request, HTTP status code,
              access token, and token type or an error message.
    """
    try:
        # Use Pyrebase to sign in with email and password
        user = AUTH_PROVIDER.auth().sign_in_with_email_and_password(data.email, data.password)
        
        # Get the ID token after successful authentication
        token = user["idToken"]

        return {
            "status": "success",
            "status_code": 200,
            "access_token": token,
            "token_type": "bearer"
        }
    except Exception as e:
        # Return sanitized error message
        return {
            "status": "error",
            "status_code": 400,
            "msg": "Invalid email or password." if "EMAIL_NOT_FOUND" in str(e) or "INVALID_PASSWORD" in str(e) else "An error occurred."
        }

async def signup_controller(data: SignUpSchema) -> dict:
    """
    Handle user sign-up by creating a new user with email and password using Pyrebase.

    Args:
        data (SignUpSchema): The sign-up data containing email and password.

    Returns:
        dict: A dictionary containing the status of the request, HTTP status code,
              access token, and token type or an error message.
    """
    try:
        # Use Pyrebase to sign up with email and password
        user = AUTH_PROVIDER.auth().create_user_with_email_and_password(data.email, data.password)
        
        # Get the ID token after successful registration
        token = user["idToken"]

        return {
            "status": "success",
            "status_code": 200,
            "access_token": token,
            "token_type": "bearer"
        }
    except Exception as e:
        # Return sanitized error message
        return {
            "status": "error",
            "status_code": 400,
            "msg": "User already exists." if "EMAIL_EXISTS" in str(e) else "An error occurred."
        }
    
async def signout_controller() -> dict:
    """
    Handle user sign-out. This function mainly serves as a placeholder,
    as actual sign-out functionality (e.g., token removal) is typically handled on the client side.

    Returns:
        dict: A dictionary indicating the success or failure of the sign-out process.
    """
    try:
        # Since sign_out() is a client-side function in Pyrebase, it won't work on the backend
        # Token revocation is generally handled on the client side by removing it from storage.
        AUTH_PROVIDER.auth().current_user = None
        return {
            "status": "success",
            "status_code": 200,
            "msg": "Sign out successful (handled on the client)."
        }
    except Exception as e:
        return {
            "status": "error",
            "status_code": 400,
            "msg": str(e)
        }
    
async def ping_controller(data: TokenSchema) -> dict:
    """
    Verify the validity of the provided token by checking it with Pyrebase.

    Args:
        data (TokenSchema): The token data containing the access token to be verified.

    Returns:
        dict: A dictionary containing the status of the request, HTTP status code,
              message, and user information if the token is valid or an error message if invalid.
    """
    try:
        # Use Pyrebase to verify the ID token
        user = AUTH_PROVIDER.auth().get_account_info(data.access_token)
        
        return {
            "status": "success",
            "status_code": 200,
            "msg": "Ping successful",
            "user_info": user
        }
    except Exception as e:
        return {
            "status": "error",
            "status_code": 400,
            "msg": "Invalid token." if "INVALID_ID_TOKEN" in str(e) else "An error occurred."
        }
