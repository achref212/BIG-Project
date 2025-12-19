from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # === APP ===
    app_name: str = "EduApp"
    env: str = "development"
    debug: bool = True

    # === SECURITY / JWT ===
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # === DATABASE ===
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    database_url: str | None = None

    # === MAIL ===
    mail_host: str
    mail_port: int
    mail_username: str
    mail_password: str
    mail_from: str

    # === STORAGE ===
    storage_provider: str = "local"
    storage_path: str = "uploads/"

    # === WEBSOCKET / MULTIPLAYER ===
    websocket_enabled: bool = True
    room_code_length: int = 6

    # === PAGINATION ===
    default_page_size: int = 10
    max_page_size: int = 100

    class Config:
        env_file = ".env"
        extra = "forbid"  # 🔒 sécurité maximale


settings = Settings()
