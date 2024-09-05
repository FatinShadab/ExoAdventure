"""
settings package

This package handles the configuration settings for the application. It includes:

- core.py: Manages the core configuration settings, including environment variables, Firebase credentials, and application defaults.
- firebase.py: Initializes and configures Firebase with credentials and database URL, and sets up security with HTTPBearer.
- middleware.py: Defines Middleware like CORS settings for handling cross-origin requests, including allowed origins, methods, and headers.

Modules:
- core: Contains essential configurations such as Firebase credentials, frontend URL, and environment settings.
- firebase: Initializes Firebase services and handles authentication.
- middleware: Configures Middleware like CORS settings to manage cross-origin requests and security.

Usage:
- Import settings from this package to access configuration values, initialize services, and set up middleware for the application.

Example:
    from settings.core import FRONTEND_URL
    from settings.firebase import FIREBASE_APP
    from settings.middleware import cors_settings

Notes:
- Ensure that environment variables are properly set and the .env file is correctly loaded.
- Configuration should be reviewed and adjusted according to the deployment environment and application needs.
"""
