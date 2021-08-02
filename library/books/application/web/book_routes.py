import uuid

from flask import Blueprint

from library.books.application.config.containers import Container
from library.books.application.web.book_controller import BookController

books_routes = Blueprint("books_routes", __name__)

container = Container()

controller = BookController(service=container.service)


@books_routes.route("/books/<string:book_id>", methods=['GET'])
def get_book_by_id(book_id):
    return controller.find_by(book_id)


@books_routes.route("/books", methods=['POST'])
def create_book():
    return controller.create()


@books_routes.route("/books/<string:book_id>", methods=['PUT'])
def update_book(book_id):
    return controller.update(book_id)
