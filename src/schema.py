import strawberry
from typing import List
from datetime import datetime
from repository import get_books, create_book
from pydantic import BaseModel

def get_author_for_book(root) -> "Author":
    return Author(name="Michaeil Crichton")


@strawberry.type
class Book:
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)


def get_books_for_author(root):
    return [Book(title="Jurassic Park")]


@strawberry.type
class Author:
    name: str
    books: List[Book] = strawberry.field(resolver=get_books_for_author)


def get_authors(root) -> List[Author]:
    return [Author(name="Michael Crichton")]


@strawberry.type
class BookDb:
    id: int
    name: str
    publication_date: str


@strawberry.type
class Query:
    authors: List[Author] = strawberry.field(resolver=get_authors)
    books: List[Book] = strawberry.field(resolver=get_books_for_author)
    books_from_db: List[BookDb] = strawberry.field(resolver=get_books)


# @strawberry.input
# class AddBookInput:
#     name: str

@strawberry.input
class AddBookInput:
    name: str
    publication_date: datetime
    author_id: int



@strawberry.type
class Mutation:
    @strawberry.field()
    async def add_book(self, book: AddBookInput) -> Book:
        book = await create_book(book)
        return book


schema = strawberry.Schema(query=Query, mutation=Mutation)
