"""
auth.py

Schemas for authentication-related data in the application.

This module defines Pydantic models to validate and serialize data
related to user authentication, including sign-in, sign-up, and token
management.

Classes:
- SignInSchema: Schema for user sign-in data.
- SignUpSchema: Schema for user sign-up data.
- TokenSchema: Schema for authentication tokens.

Classes:
1. SignInSchema(BaseModel):
    - email (str): User's email address. Must be provided. Example: "jondoe123@gmail.com".
    - password (str): User's password. Must be provided. Example: "password123".

2. SignUpSchema(BaseModel):
    - email (str): User's email address. Must be provided. Example: "jondoe123@gmail.com".
    - password (str): User's password. Must be provided. Example: "password123".

3. TokenSchema(BaseModel):
    - access_token (str): The access token issued after successful authentication. Must be provided. Example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c".
    - token_type (str): The type of the token, typically "bearer". Must be provided. Example: "bearer".
"""

from pydantic import BaseModel, Field


class SignInSchema(BaseModel):
    """
    Schema for user sign-in data.

    Attributes:
    - email (str): User's email address. Must be provided.
    - password (str): User's password. Must be provided.
    """
    email: str = Field(..., example="jondoe123@gmail.com")
    password: str = Field(..., example="password123")


class SignUpSchema(BaseModel):
    """
    Schema for user sign-up data.

    Attributes:
    - email (str): User's email address. Must be provided.
    - password (str): User's password. Must be provided.
    """
    email: str = Field(..., example="jondoe123@gmail.com")
    password: str = Field(..., example="password123")


class TokenSchema(BaseModel):
    """
    Schema for authentication tokens.

    Attributes:
    - access_token (str): The access token issued after successful authentication. Must be provided.
    - token_type (str): The type of the token, typically "bearer". Must be provided.
    """
    access_token: str = Field(..., example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    token_type: str = Field(..., example="bearer")