from flask_restful import reqparse
from flask_restful.reqparse import Namespace

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, help="Name of book is required", required=True)
parser.add_argument("pages", type=int, help="Amount of book's pages is required", required=True)
parser.add_argument("isbn", type=str, help="ISBN of book is required", required=True)


class CreateBookRequest:
    name: str
    pages: int
    isbn: str

    def __init__(self, json: Namespace):
        self.name = json.get("name")
        self.pages = json.get("pages")
        self.isbn = json.get("isbn")
