import uuid


class Person:
    id = str(uuid.uuid4())
    username: str
    password: str

    def __init__(self, username, password):
        self.username = username
        self.password = password
