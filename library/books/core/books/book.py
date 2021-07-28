import uuid

from library.books.application.web.requests.create_book_request import CreateBookRequest


class Book:
    id = uuid.uuid4()
    name = str
    pages = int
    isbn = str

    def __init__(self, name, pages, isbn):
        self.name = name
        self.pages = pages
        self.isbn = isbn

    @classmethod
    def create(cls, request: CreateBookRequest):
        return Book(request.name, request.pages, request.isbn)

    def update(self, request):
        self.name = request.name if request.name is None else self.name
        self.pages = request.pages if request.name is None else self.pages
        self.isbn = request.isbn if request.name is None else self.isbn

        return self
