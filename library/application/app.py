from flask import Flask
from flask_restful import Api
from injector import Injector

from library.application.books.book_module import BookModule
from library.view.books.book_controller import BookController
from library.view.books.book_routes import book_routes
from library.view.error_handler import error_handler

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    injector = Injector([BookModule])

    book_routes(app, injector.get(BookController))
    error_handler(app)

    app.run(host="0.0.0.0", port=8080, debug=True)
