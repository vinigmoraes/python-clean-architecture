import dataclasses


@dataclasses.dataclass
class UpdateBookDTO:
    name: str
    pages: int
    isbn: str

    @classmethod
    def from_json(cls, json):
        return cls(
            name=json['name'],
            pages=json['pages'],
            isbn=json['isbn']
        )
