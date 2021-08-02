from flask import request
from flask_restful import Resource

from library.books.application.web.requests.create_book_request import CreateBookRequest
from library.books.application.web.requests.update_book_request import UpdateBookRequest
from library.books.application.web.responses import book_found_response
from library.books.application.web.responses.book_created_response import BookCreatedResponse
from library.books.core.books.book_service import BookService


class BookController(Resource):
    def __init__(self, service: BookService):
        self.service = service

    def find_by(self, book_id: str):
        book = self.service.find_by_id(book_id)

        return book_found_response.create(book), 200

    def create(self):
        json = request.get_json()

        create_book_request = CreateBookRequest(json)

        book = self.service.create_book(create_book_request)

        return BookCreatedResponse.create(book.id), 201

    def update(self, book_id: str):
        json = request.get_json()

        update_book_request = UpdateBookRequest(json)

        self.service.update_book(book_id, update_book_request)

        return 204
