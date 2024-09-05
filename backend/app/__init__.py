"""
This file initializes the FastAPI app for the project.

In Python packages, the `__init__.py` file is used to initialize a package as a module, and here it is being used
to expose the FastAPI app instance (`APP`) from the `main.py` module.

By importing `app` as `APP`, this file makes the application instance available at the package level.
This allows other parts of the project (or external tools like `uvicorn`) to run the app by referencing the package.

Example:
    This allows you to run the FastAPI app with a command like:
    
    ```bash
    uvicorn my_project:APP
    ```

Attributes:
    APP (FastAPI): The FastAPI application instance imported from the `main.py` module.
"""

# Import the FastAPI application instance from `main.py` and expose it as `APP`
from .main import app as APP