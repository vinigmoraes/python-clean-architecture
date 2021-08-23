import hmac

from flask import request, jsonify
from flask_jwt_extended import create_access_token
from injector import inject

from library.domain.persons.repository.person_repository import PersonRepository


class AuthController:

    @inject
    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def login(self):
        username = request.json.get("username")
        password = request.json.get("password")

        person = self.repository.find_by_username(username)

        if person and hmac.compare_digest(person.password, password):
            claims = {"role": person.role.value}

            access_token = create_access_token(
                identity=username,
                additional_claims=claims
            )

            return jsonify(acess_token=access_token)
