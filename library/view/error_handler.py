import json

from library.view.books.schemas.schema_validation_exception import SchemaValidationException


def error_handler(app):
    @app.errorhandler(SchemaValidationException)
    def bad_request(e):
        return json.dumps({"errors": e.errors}), e.status_code
