from dataclasses import dataclass

from dataclasses_json import dataclass_json

from library.domain.books.book import Book


@dataclass_json
@dataclass
class BookFoundResponse:
    id: str
    name: str
    pages: int
    isbn: str

    @classmethod
    def from_book(cls, book: Book):
        return cls(
            id=book.id,
            name=book.name,
            pages=book.pages,
            isbn=book.isbn
        )
