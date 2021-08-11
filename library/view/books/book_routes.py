from flask_expects_json import expects_json

from library.view.books.book_controller import BookController
from library.view.books.schemas.schemas import CREATE_BOOK_SCHEMA


def book_routes(app, controller: BookController):
    @app.route("/books/<string:book_id>", methods=['GET'])
    def get_book_by_id(book_id):
        return controller.find_by(book_id)

    @app.route("/books", methods=['POST'])
    @expects_json(CREATE_BOOK_SCHEMA)
    def create_book():
        return controller.create()

    @app.route("/books/<string:book_id>", methods=['PUT'])
    def update_book(book_id):
        return controller.update(book_id)
