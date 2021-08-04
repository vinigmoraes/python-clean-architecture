from flask_restful import reqparse
from flask_restful.reqparse import Namespace

from library.books.core.books.ports.dto.update_book_dto import UpdateBookDTO

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, help="Name of book is required", required=False)
parser.add_argument("pages", type=int, help="Amount of book's pages is required", required=False)
parser.add_argument("isbn", type=str, help="ISBN of book is required", required=False)


class UpdateBookRequest:
    name: str
    pages: int
    isbn: str

    def __init__(self, json: Namespace):
        self.name = json.get("name")
        self.pages = json.get("pages")
        self.isbn = json.get("isbn")

    def to_dto(self) -> UpdateBookDTO:
        return UpdateBookDTO(
            name=self.name,
            pages=self.pages,
            isbn=self.isbn
        )