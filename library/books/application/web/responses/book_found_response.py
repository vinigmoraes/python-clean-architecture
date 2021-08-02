from flask import jsonify

from library.books.core.books.book import Book


def create(book: Book):
    return jsonify(
        id=book.id,
        name=book.name,
        pages=book.pages,
        isbn=book.isbn
    )
