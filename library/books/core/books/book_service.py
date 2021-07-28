import uuid

from library.books.application.web.requests.create_book_request import CreateBookRequest
from library.books.application.web.requests.update_book_request import UpdateBookRequest
from library.books.core.books.book import Book
from library.books.core.books.ports.book_repository import BookRepository


class BookService:

    repository: BookRepository

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, request: CreateBookRequest) -> Book:
        book: Book = Book.create(request)

        self.repository.save(book)

        return book

    def find_by_id(self, book_id: uuid) -> Book:
        book = self.repository.find_by_id(book_id)

        return book

    def update_book(self, book_id: uuid, request: UpdateBookRequest):
        book: Book = self.repository.find_by_id(book_id)

        updated_book = book.update(request)

        self.repository.find_and_replace(book.id, updated_book)
