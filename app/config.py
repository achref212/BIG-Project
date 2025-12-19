from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    # ───────── DATABASE ─────────
    DATABASE_URL: str

    # ───────── SECURITY / JWT ─────────
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # ───────── EMAIL ─────────
    MAIL_HOST: str | None = None
    MAIL_PORT: int | None = None
    MAIL_USERNAME: str | None = None
    MAIL_PASSWORD: str | None = None
    MAIL_FROM: str | None = None

    # ───────── OPTIONAL / FLAGS ─────────
    DEBUG: bool = False

    # 🔑 Pydantic v2 config
    model_config = ConfigDict(
        env_file=".env",
        extra="allow"   # <<< LA LIGNE QUI RÉSOUT TOUT
    )


settings = Settings()
