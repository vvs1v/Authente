from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings
from urllib.parse import quote_plus 
from config import settings

encoded_user = quote_plus(settings.DB_USER)
encoded_password = quote_plus(settings.DB_PASSWORD)

# SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
DATABASE_URL = f"postgresql+asyncpg://{encoded_user}:{encoded_password}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_async_engine(
    # SQLALCHEMY_DATABASE_URL,
    DATABASE_URL,
    echo=True
    # connect_args={"check_same_thread": False},
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session