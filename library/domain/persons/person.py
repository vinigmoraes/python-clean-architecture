import uuid

from library.domain.persons.person_role import PersonRole


class Person:
    id = str(uuid.uuid4())
    username: str
    password: str
    role: PersonRole

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
