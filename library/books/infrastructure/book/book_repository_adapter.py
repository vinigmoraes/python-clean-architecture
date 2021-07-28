import uuid

from library.books.core.books.book import Book
from library.books.core.books.ports.book_repository import BookRepository


class BookRepositoryAdapter(BookRepository):
    repository = [
        Book("Lord of The ring", 200, "8ac2faba-a5dc-4fe4-8236-f01490221c8c"),
        Book("Clean Code", 350, "b2b1cdf2-bcb2-4e9c-80df-6d7f000b16dc")
    ]

    def save(self, book: Book):
        self.repository.append(book)

    def find_by_id(self, book_id: uuid) -> Book:
        for book in self.repository:
            if book.id == book_id:
                return book

    def find_and_replace(self, book_id: uuid, new_book: Book) -> Book:
        index = self.repository.index(book_id)

        self.repository[index] = new_book

        return new_book
