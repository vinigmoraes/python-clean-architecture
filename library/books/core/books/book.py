import uuid

from library.books.core.books.ports.dto.create_book_dto import CreateBookDTO
from library.books.core.books.ports.dto.update_book_dto import UpdateBookDTO


class Book:
    id = uuid.uuid4()
    name = str
    pages = int
    isbn = str

    def __init__(self, name, pages, isbn):
        self.name = name
        self.pages = pages
        self.isbn = isbn

    @classmethod
    def create(cls, dto: CreateBookDTO):
        return cls(dto.name, dto.pages, dto.isbn)

    def update(self, dto: UpdateBookDTO):
        self.name = dto.name if dto.name is None else self.name
        self.pages = dto.pages if dto.name is None else self.pages
        self.isbn = dto.isbn if dto.name is None else self.isbn

        return self
