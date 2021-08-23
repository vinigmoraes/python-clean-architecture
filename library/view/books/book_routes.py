from library.application.auth.admin_required import admin_required
from library.view.books.book_controller import BookController


def book_routes(app, controller: BookController):
    @app.route("/books/<string:book_id>", methods=['GET'])
    def get_book_by_id(book_id):
        return controller.find_by(book_id)

    @app.route("/books", methods=['POST'])
    @admin_required()
    def create_book():
        return controller.register()

    @app.route("/books/<string:book_id>", methods=['PUT'])
    def update_book(book_id):
        return controller.update(book_id)
