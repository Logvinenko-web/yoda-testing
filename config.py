from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int
    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expires_s: int = 3600
    database_url: str


settings = Settings(
    _env_file='.env.example',
    _env_file_encoding='utf-8'
)
