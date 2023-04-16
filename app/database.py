from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from config import DatabaseBaseSettings, db_root_settings
from typing import Any
from ujson import loads, dumps

###
# Database Engines
###


# Engine generator
def create_custom_async_engine(db_settings: DatabaseBaseSettings, **kwargs: Any) -> Any:
    """Generates a valid SQLModel engine compatible with SQLAlchemy from a provided datgabase settings object."""
    return create_async_engine(
        url=db_settings.create_async_postgres_uri(),
        max_overflow=db_settings.engine_max_overflow,
        pool_size=db_settings.engine_pool_size,
        json_deserializer=loads,
        json_serializer=dumps,
        **kwargs,
    )


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session


# Engine callables
async_engine = create_custom_async_engine(db_root_settings)
