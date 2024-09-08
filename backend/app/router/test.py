"""
This module is part of the `router` package and defines a simple test route for the FastAPI application.

The `test.py` module contains a single route (`/test`) which returns a greeting message. 
This route is commonly used as a health check to ensure that the application is running correctly.

Attributes:
    router (APIRouter): The FastAPI `APIRouter` instance that is used to group and manage related routes within this module.
"""

from typing import Dict
from fastapi import APIRouter

# Create an APIRouter instance for organizing the routes in this module
router: APIRouter = APIRouter(prefix="/dev", tags=["dev"])

@router.get("/test")
def hello() -> Dict[str, str]:
    """
    A basic test route to verify if the application is functioning properly.

    This route is useful for health checks, returning a simple message to indicate that the server is up and responsive.

    Returns:
        dict: A JSON object containing a simple greeting message.
    
    Example response:
        {
            "msg": "Hello World From Fatin Shadab 🤓!"
        }
    """
    return {"msg": "Hello World From Fatin Shadab 🤓!"}
