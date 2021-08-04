import dataclasses


@dataclasses.dataclass
class CreateBookDTO:
    name: str
    pages: int
    isbn: str
