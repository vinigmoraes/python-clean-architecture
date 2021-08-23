from library.domain.persons.person import Person


class PersonRepository:
    _persons = [
        Person(username="test@email.com", password="asdf")
    ]

    def find_by_username(self, username):
        for person in self._persons:
            if person.username == username:
                return person

    def find_by_id(self, person_id):
        for person in self._persons:
            if person.id == person_id:
                return person
