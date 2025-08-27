from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:admin@localhost:5432/postgres"
    POOL_SIZE: int = 10
    MAX_OVERFLOW: int = 20

    model_config = {"env_file": ".env"}

settings = Settings()