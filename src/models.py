from migration_data import Base
from sqlalchemy import (
    INTEGER,
    Column,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship


class Author(Base):
    __tablename__ = 'authors'
    id = Column(INTEGER, primary_key=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_bitrh = Column(DateTime)


class Book(Base):
    __tablename__ = "books"
    id = Column(INTEGER, primary_key=True, unique=True)
    name = Column(String, default="")
    publication_date = Column(DateTime)
    author_id = Column(INTEGER, ForeignKey("authors.id"))
    author = relationship(Author, backref="books")
