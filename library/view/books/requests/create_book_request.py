import dataclasses

from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, help="Name of book is required", required=True)
parser.add_argument("pages", type=int, help="Amount of book's pages is required", required=True)
parser.add_argument("isbn", type=str, help="ISBN of book is required", required=True)


@dataclasses.dataclass
class CreateBookRequest:
    name: str
    pages: int
    isbn: str
