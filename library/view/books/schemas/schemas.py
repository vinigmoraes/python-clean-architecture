CREATE_BOOK_SCHEMA = {
    "name": {"type": "string", "required": True},
    "pages": {"type": "number", "required": True},
    "isbn": {"type": "string", "required": True}
}

LOGIN_SCHEMA = {
    "username": {"type": "string", "required": True},
    "password": {"type": "string", "required": True},
}
