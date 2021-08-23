from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from injector import Injector

from library.application.books.book_module import BookModule
from library.view.auth.auth_controller import AuthController
from library.view.auth.auth_routes import auth_routes
from library.view.books.book_controller import BookController
from library.view.books.book_routes import book_routes
from library.view.error_handler import error_handler

app = Flask(__name__, instance_path="/{project_folder_abs_path}/instance")
api = Api(app)
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'some-secret'


if __name__ == '__main__':
    injector = Injector([BookModule])

    book_routes(app, injector.get(BookController))
    auth_routes(app, injector.get(AuthController))
    error_handler(app)

    app.run(host="0.0.0.0", port=8080, debug=True)
