# Project Structure

### Root Folder (`backend`)

- **`.fb_secret.json`**: Contains the Firebase private key required for Firebase authentication and authorization.
- **`.env`**: Environment variables configuration file, used to store sensitive information such as API keys, database URLs, and other settings.
- **`manager.py`**: A Django-like manager script used for managing various aspects of the FastAPI application (running commands, managing servers, etc.).
- **`requirements.txt`**: Lists the Python dependencies for the project. To install them, use: `pip install -r requirements.txt`.
- **`readme.md`**: Project documentation file (this file).

### Main Application Package (`app`)

- **`__init__.py`**: Initializes the `app` package and exports the FastAPI application instance (`APP`) from `main.py`.
- **`main.py`**: The entry point of the FastAPI application where routers, middleware, and settings are configured.
- **`router/`**: Contains user-defined routers for organizing API endpoints.
  - **`__init__.py`**: Exports all routers as a list (`ROUTERS`), which are included in the main application.
  - **`test.py`**: A test router used to verify the project setup and functionality.
  
### Settings Package (`settings/`)

The `settings` package is responsible for managing the application's configuration, including Firebase setup and middleware.

- **`__init__.py`**: A blank file to make `settings` a package.
- **`core.py`**: Handles loading environment variables, setting up defaults, and warnings. This file manages core settings like the app environment (`development`, `production`), Firebase configurations, and frontend URL.
- **`firebase.py`**: Responsible for initializing Firebase services (Firestore and Realtime Database) with FastAPI. It supports conditional usage of both Firestore and Firebase Realtime Database based on environment variable configurations.
- **`middleware.py`**: Contains the configuration for middlewares, including Cross-Origin Resource Sharing (CORS) settings.

### Firebase Setup

The project supports integration with Firebase, allowing the use of both Firestore and Realtime Database depending on the environment variables.

#### Environment Variables:
- **`FIREBASE_APP`**: The Firebase project ID.
- **`FIREBASE_CREDENTIALS_FNAME`**: The filename for the Firebase credentials (e.g., `.fb_secret.json`).
- **`FIREBASE_DB_URL`**: URL of the Firebase Realtime Database (required if using Realtime Database).
- **`FIRE_STORE`**: Set to `true` to enable Firestore.
- **`FIREBASE_RTDB`**: Set to `true` to enable Firebase Realtime Database.

#### Firebase Services:
- **Firestore**: Initialized if `FIRE_STORE` is set to `true`. It provides NoSQL cloud-based storage.
- **Realtime Database**: Initialized if `FIREBASE_RTDB` is set to `true`. It provides real-time, low-latency synchronization.

These configurations allow flexible usage of Firebase services in the platform, depending on the project needs.

---

## How to Contribute

If you want to contribute to the project, please follow these steps:

1. Clone the repository.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Configure your `.env` file with appropriate Firebase credentials and other necessary environment variables.
4. Run the FastAPI development server using the command:
   ```
   python manager.py runserver --reload
   ```
5. Make your changes and create a pull request for review.

---

### Ongoing Development

As the project is still in progress, the structure will continue to expand with additional features, services, and improvements. Stay tuned for further updates and documentation!
