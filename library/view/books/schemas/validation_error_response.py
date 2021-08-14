from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from library.view.books.schemas.error import Error


@dataclass_json
@dataclass
class ValidationErrorResponse:
    errors: List[Error]
