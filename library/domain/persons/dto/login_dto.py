from dataclasses import dataclass


@dataclass
class LoginDTO:
    username: str
    password: str

    @classmethod
    def from_json(cls, json):
        return cls(
            username=json['username'],
            password=json['password']
        )
