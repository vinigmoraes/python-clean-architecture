import dataclasses


@dataclasses.dataclass
class CreateBookDTO:
    name: str
    pages: int
    isbn: str

    @classmethod
    def from_json(cls, json):
        return cls(
            name=json.get('name'),
            pages=json.get('pages'),
            isbn=json.get('isbn')
        )