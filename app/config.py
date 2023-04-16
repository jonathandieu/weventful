from pydantic import BaseSettings


###
# Global Settings
###
class BaseConfigurationModel(BaseSettings):
    class Config(BaseSettings.Config):
        env_file_encoding = "utf-8"
        case_sensitive = False


###
# Database Settings
###


# Common Database Connection Settings
class DatabaseBaseSettings(BaseConfigurationModel):
    """Base class for database config instances."""

    host: str
    port: int
    name: str
    user: str
    password: str
    engine_pool_size: int = 100
    engine_max_overflow: int = 0

    def create_postgres_uri(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    def create_async_postgres_uri(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    class Config(BaseConfigurationModel.Config):
        env_prefix: str = "DB_"


class DatabaseWriteSettings(DatabaseBaseSettings):
    """Database configuration for leader / write connections."""

    class Config(BaseConfigurationModel.Config):
        env_prefix = "DB_WRITE_"


# Constant exports
db_root_settings = DatabaseBaseSettings()
