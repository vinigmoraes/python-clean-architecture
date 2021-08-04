import dataclasses


@dataclasses.dataclass
class UpdateBookDTO:
    name: str
    pages: int
    isbn: str