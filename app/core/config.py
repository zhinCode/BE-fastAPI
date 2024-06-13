from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_port: int
    database_host: str
    database_port: int
    database_user: str
    database_password: str
    database_name: str
    mongo_host: str
    mongo_port: int
    mongo_user: str
    mongo_password: str
    mongo_db_name: str
    app_version: str
    app_author: str

    class Config:
        env_file = ".env"

settings = Settings()
