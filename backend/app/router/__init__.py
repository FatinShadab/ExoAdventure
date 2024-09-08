"""
This `__init__.py` file is part of the `router` package, which organizes and exports all route modules for the FastAPI application.

Purpose:
    The file imports routers from various route modules (such as `test.py` and `auth.py`) and consolidates them into a list called `ROUTERS`. This list is then used to include all the route modules in the main FastAPI application.

Attributes:
    ROUTERS (List[APIRouter]): A list of FastAPI `APIRouter` instances, each representing a set of routes from different route modules. This list simplifies route registration and management in the main application.

Routers Included:
    - `test_router`: Handles routes defined in the `test.py` module.
    - `auth_router`: Handles routes defined in the `auth.py` module.
"""

from typing import List
from fastapi import APIRouter

# Import the routers from different route modules
from .test import router as test_router
from .auth import router as auth_router

# List of routers to be included in the FastAPI app
ROUTERS: List[APIRouter] = [
    test_router,  # Router for `/test` routes
    auth_router,  # Router for `/auth` routes
]
