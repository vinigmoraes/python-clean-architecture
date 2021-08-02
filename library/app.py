from flask import Flask
from flask_restful import Api

from library.books.application.config.containers import Container
from library.books.application.web.book_routes import books_routes

app = Flask(__name__)
api = Api(app)

app.register_blueprint(books_routes)

if __name__ == '__main__':
    container = Container()
    container.init_resources()

    app.run(port=8080)
    app.container = container
