import dataclasses

import dataclasses_json

from library.domain.books.book import Book


@dataclasses_json.dataclass_json
@dataclasses.dataclass
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
