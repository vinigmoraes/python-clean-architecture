from flask import request
from flask_restful import Resource

from library.books.application.web.requests.create_book_request import CreateBookRequest
from library.books.application.web.requests.update_book_request import UpdateBookRequest
from library.books.application.web.responses.book_created_response import BookCreatedResponse
from library.books.application.web.responses.book_found_response import BookFoundResponse
from library.books.core.books.book_service import BookService
from library.books.infrastructure.book.book_repository_adapter import BookRepositoryAdapter


class BookController(Resource):
    service = BookService(repository=BookRepositoryAdapter())

    def get(self, book_id: str):
        book = self.service.find_by_id(book_id)

        return BookFoundResponse.create(book), 200

    def post(self):
        json = request.get_json()

        create_book_request = CreateBookRequest(json)

        book = self.service.create_book(create_book_request)

        return BookCreatedResponse.create(book.id), 201

    def update(self, book_id: str):
        json = request.get_json()

        update_book_request = UpdateBookRequest(json)

        self.service.update_book(book_id, update_book_request)

        return 204