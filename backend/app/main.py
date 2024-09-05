from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing routers and CORS settings from the project
from .router import ROUTERS  # List of FastAPI routers
from .settings.middleware import cors_settings  # Dictionary with CORS middleware settings

# Initialize FastAPI application
app: FastAPI = FastAPI()

# Add CORS middleware to the FastAPI app
# This enables cross-origin resource sharing (CORS), allowing your app to accept requests from different domains.
app.add_middleware(
    CORSMiddleware,
    **cors_settings  # Expanding the CORS settings from the imported dictionary
)

# Include all routers from the imported ROUTERS list
# ROUTERS is expected to be a list of FastAPI APIRouter objects.
# We iterate over each router and include them in the FastAPI app.
for router in ROUTERS:  # type: List[APIRouter]
    app.include_router(router)
