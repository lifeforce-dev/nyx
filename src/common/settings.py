from pydantic import BaseModel

class AppSettings(BaseModel):
    base_url: str = "http://localhost:8000"
    port: int = 8000

APP_SETTINGS = AppSettings()
