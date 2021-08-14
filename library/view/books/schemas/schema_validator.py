from cerberus import Validator

from library.view.books.schemas.schema_validation_exception import SchemaValidationException


def validate_json(schema, json):
    validator = Validator(schema)

    if not validator.validate(json):
        raise SchemaValidationException(validator.errors)