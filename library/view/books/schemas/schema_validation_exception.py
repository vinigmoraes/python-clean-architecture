from typing import List

from werkzeug.exceptions import BadRequest


class SchemaValidationException(BadRequest):
    status_code = 400
    errors: List[str]

    def __init__(self, errors):
        self.errors = errors