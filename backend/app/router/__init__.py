"""
This `__init__.py` file is part of the `router` package, responsible for organizing and exporting all route modules.

The purpose of this file is to import routers from different route modules (like `test.py`) and 
collect them in a list (`ROUTERS`). This list can then be included in the main FastAPI app.

By consolidating all routers in this file, it makes it easier to manage and maintain route registration in the main application.

Attributes:
    ROUTERS (list): A list of FastAPI `APIRouter` instances that are collected from various route modules.
"""

from typing import List
from fastapi import APIRouter

# Import the `test_router` from the `test.py` module and alias it to `test_router`
from .test import router as test_router

# List of routers to be included in the FastAPI app
ROUTERS: List[APIRouter] = [
    test_router  # This router handles the `/test` route from the `test.py` module
]
