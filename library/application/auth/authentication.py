import hmac

from library.domain.persons.repository.person_repository import PersonRepository

repository = PersonRepository()


def authenticate(username, password):
    person = repository.find_by_username(username)

    if person and hmac.compare_digest(person.password, password):
        return person


def identity(payload):
    person_id = payload['identity']
    return repository.find_by_id(person_id)
