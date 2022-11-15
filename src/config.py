from pydantic import BaseSettings, Field, SecretStr


class AdvanceBaseSettings(BaseSettings):
    """
    Родительский класс настроек
    """

    class Config:
        allow_mutation = False


class ServiceDatabseSetting(AdvanceBaseSettings):
    host: str
    username: str
    password: str
    db_name: str = Field(..., env="")
    port: int = Field(default="5432")
    container_name: str

    class Config:
        env_prefix = "service_db_"

    @property
    def postgresql_url(self) -> str:
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.container_name}:{self.port}/{self.db_name}"
