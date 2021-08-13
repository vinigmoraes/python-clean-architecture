from flask import Flask
from flask_restful import Api
from injector import Injector

from library.application.books.book_module import BookModule
from library.view.books.book_controller import BookController
from library.view.books.book_routes import book_routes

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    injector = Injector([BookModule])

    book_routes(app, injector.get(BookController))

    app.run(host="0.0.0.0", port=8080, debug=True)
