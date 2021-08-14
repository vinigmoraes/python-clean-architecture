from flask import request
from flask_restful import Resource
from injector import inject

from library.application.books.book_service import BookService
from library.domain.books.ports.dto.create_book_dto import CreateBookDTO
from library.domain.books.ports.dto.update_book_dto import UpdateBookDTO
from library.view.books.responses.book_created_response import BookCreatedResponse
from library.view.books.responses.book_found_response import BookFoundResponse
from library.view.books.schemas.schema_validator import validate_json
from library.view.books.schemas.schemas import CREATE_BOOK_SCHEMA


class BookController(Resource):

    @inject
    def __init__(self, service: BookService):
        self.service = service

    def find_by(self, book_id: str):
        book = self.service.find_by_id(book_id)

        return BookFoundResponse.from_book(book).to_json(), 200

    def create(self):
        json = request.get_json()

        validate_json(CREATE_BOOK_SCHEMA, json)

        dto = CreateBookDTO.from_json(json)

        book = self.service.create_book(dto)

        return BookCreatedResponse(id=book.id).to_json(), 201

    def update(self, book_id: str):
        json = request.get_json()

        dto = UpdateBookDTO.from_json(json)

        self.service.update_book(book_id, dto)

        return 204
