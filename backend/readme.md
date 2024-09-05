# Project Structure

### Root Folder (`backend`)

- **`.fb_secret.json`**: Contains the Firebase private key required for authentication and authorization with Firebase services.
- **`.env`**: Environment variables file for configuring settings such as database URLs, API keys, and other sensitive information.
- **`manager.py`**: A Django-like manager script used to run commands or manage various aspects of the project.
- **`requirements.txt`**: Lists the Python packages and dependencies required for the project. Use this file to install dependencies with `pip install -r requirements.txt`.
- **`readme.md`**: This documentation file, which provides an overview and instructions for the project.

### Main Application Package (`app`)

- **`__init__.py`**: Initializes the `app` package and exports the FastAPI application instance (`APP`) from `main.py`.
- **`main.py`**: The entry point of the FastAPI application. This file assembles and configures the FastAPI application, integrating routers and settings.
- **`router/`**: Contains user-defined routers for organizing API routes.
  - **`__init__.py`**: Exports all routers as a list (`ROUTERS`), which are included in the main application.
  - **`test.py`**: A test router used to verify the setup of the project and test functionality.
- **`settings/`**: Manages configuration settings for the project.
  - **`__init__.py`**: Blank file to make `settings` a package.
  - **`core.py`**: Handles core configuration, including reading environment variables from `.env`.
  - **`firebase.py`**: Initializes Firebase settings and objects, making Firebase services available throughout the application.
  - **`middleware.py`**: Configures middleware settings, such as CORS settings, to manage cross-origin requests and security.