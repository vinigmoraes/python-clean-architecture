import uuid

from flask import jsonify


class BookCreatedResponse:

    @staticmethod
    def create(book_id: uuid):
        return jsonify(id=book_id)
