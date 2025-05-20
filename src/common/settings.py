from pydantic import BaseSettings

class AppSettings(BaseSettings):
    base_url: str = "http://localhost:8000"
    port: int = 8000
    log_level: str = "debug"

APP_SETTINGS = AppSettings()
