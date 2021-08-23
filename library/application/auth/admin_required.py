from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request

from library.domain.persons.person_role import PersonRole


def admin_required():
    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()

            if claims['role'] == PersonRole.ADMIN.value:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="You are not authorized to execute this request"), 403

        return decorator

    return wrapper

