import json

from flask import Response

from library.view.books.schemas.schema_validation_exception import SchemaValidationException


def error_handler(app):
    @app.errorhandler(SchemaValidationException)
    def bad_request(e):
        return Response(response=json.dumps({"message": e.message, "errors": e.errors}),
                        status=e.status_code,
                        mimetype="application/json")
