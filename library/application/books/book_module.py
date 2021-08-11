from injector import singleton, Module

from library.application.books.book_service import BookService
from library.domain.books.ports.book_repository import BookRepository
from library.infrastructure.book.book_repository_adapter import BookRepositoryAdapter
from library.view.books.book_controller import BookController


class BookModule(Module):

    def configure(self, binder):
        binder.bind(BookRepository, to=BookRepositoryAdapter, scope=singleton)
        binder.bind(BookService, to=BookService, scope=singleton)
        binder.bind(BookController, to=BookController, scope=singleton)
