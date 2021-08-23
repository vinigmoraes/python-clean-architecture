from injector import Module, singleton

from library.domain.persons.repository.person_repository import PersonRepository
from library.view.auth.auth_controller import AuthController


class AuthModule(Module):

    def configure(self, binder):
        binder.bind(PersonRepository, to=PersonRepository, scope=singleton)
        binder.bind(AuthController, to=AuthController, scope=singleton)
