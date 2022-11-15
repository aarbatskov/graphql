import os
from config import ServiceDatabseSetting
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

service_datbase_settings = ServiceDatabseSetting(
    host=os.getenv("POSTGRES_HOST"),
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    db_name=os.getenv("POSTGRES_DB"),
    port=os.getenv("POSTGRES_PORT"),
    container_name=os.getenv("DB_NAME")
)

engine = create_async_engine(
    service_datbase_settings.postgresql_url,
    echo=True,
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def get_db():
    return async_session()


Base = declarative_base()
