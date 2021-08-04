from flask import request
from flask_restful import Resource

from library.books.application.web.requests.create_book_request import CreateBookRequest
from library.books.application.web.requests.update_book_request import UpdateBookRequest
from library.books.application.web.responses.book_created_response import BookCreatedResponse
from library.books.application.web.responses.book_found_response import BookFoundResponse
from library.books.core.books.book_service import BookService


class BookController(Resource):
    def __init__(self, service: BookService):
        self.service = service

    def find_by(self, book_id: str):
        book = self.service.find_by_id(book_id)

        return BookFoundResponse.create(book), 200

    def create(self):
        json = request.get_json()

        dto = CreateBookRequest(json).to_dto()

        book = self.service.create_book(dto)

        return BookCreatedResponse.create(book.id), 201

    def update(self, book_id: str):
        json = request.get_json()

        dto = UpdateBookRequest(json).to_dto()

        self.service.update_book(book_id, dto)

        return 204
