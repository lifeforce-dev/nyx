from fastapi import FastAPI
from backend.routes.api.core import router as api_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app
