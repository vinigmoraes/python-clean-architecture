from dependency_injector import containers, providers

from library.books.application.web.book_controller import BookController
from library.books.core.books.book_service import BookService
from library.books.core.books.ports.book_repository import BookRepository
from library.books.infrastructure.book.book_repository_adapter import BookRepositoryAdapter


class Container(containers.DeclarativeContainer):
    repository = providers.AbstractFactory(BookRepository)
    repository.override(providers.Factory(BookRepositoryAdapter))

    service = providers.Factory(
        BookService,
        repository=repository
    )

    controller = providers.Factory(
        BookController,
        service=service
    )
