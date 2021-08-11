import uuid

from injector import inject

from library.domain.books.book import Book
from library.domain.books.ports.book_repository import BookRepository
from library.domain.books.ports.dto.create_book_dto import CreateBookDTO
from library.domain.books.ports.dto.update_book_dto import UpdateBookDTO


class BookService:

    @inject
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, dto: CreateBookDTO) -> Book:
        book: Book = Book.create(dto)

        self.repository.save(book)

        return book

    def find_by_id(self, book_id: uuid) -> Book:
        book: Book = self.repository.find_by_id(book_id)

        return book

    def update_book(self, book_id: uuid, dto: UpdateBookDTO):
        book: Book = self.repository.find_by_id(book_id)

        updated_book = book.update(dto)

        self.repository.find_and_replace(book.id, updated_book)
