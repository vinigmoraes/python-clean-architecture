CREATE_BOOK_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "pages": {"type": "number"},
        "isbn": {"type": "string"},
    },
    "required": ["name", "pages", "isbn"]
}
