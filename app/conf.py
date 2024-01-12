from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env", env_file_encoding="utf-8", extra="ignore"
    )

    redis_url: str
    celery_broker_url: str
    celery_backend_url: str


settings = Settings()
