from jsonschema import Draft7Validator

from library.view.books.schemas.error import Error
from library.view.books.schemas.schema_validation_exception import SchemaValidationException


def validate_json(schema, json):
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(json), key=lambda e: e.path)

    validation_errors = []

    for error in errors:
        validation_errors.append(error.message)

    raise SchemaValidationException(validation_errors)
