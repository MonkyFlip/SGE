from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Base de datos
    DATABASE_URL: str

    # JWT (si lo usarás)
    SECRET_KEY: str = "supersecret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Configuración general
    APP_NAME: str = "SGE Backend"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
