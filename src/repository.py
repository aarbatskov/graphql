from db import get_db
from sqlalchemy import select, insert
from models import Book

async def get_books():
    async with get_db() as session:
        result = await session.execute(
            select(Book)

        )
        session.commit()
        books = result.scalars().all()
        return books


async def create_book(book_data):
    async with get_db() as session:
        result = await session.execute(
            insert(Book).
            values(name=book_data.name,
                   publication_date=book_data.publication_date,
                   author_id=book_data.author_id
                   ).
            returning(*Book.__table__.c)
        )
        book = result.first()
        await session.commit()
        return book