import uuid

from library.domain.books.book import Book


class BookRepository:

    def save(self, book: Book):
        pass

    def find_by_id(self, book_id: uuid) -> Book:
        pass

    def find_and_replace(self, book_id: uuid, new_book: Book) -> Book:
        pass
