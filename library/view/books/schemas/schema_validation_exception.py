from typing import List

from werkzeug.exceptions import BadRequest


class SchemaValidationException(BadRequest):
    status_code = 400
    message = "Invalid json sent to server"
    errors: List[str]

    def __init__(self, errors):
        self.errors = errors

