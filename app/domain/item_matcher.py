from rapidfuzz import process
from app.domain.nutrition_db import MACROS


class ItemMatcher:

    def match(
        self,
        item: str
    ):

        candidate = process.extractOne(
            item.lower(),
            MACROS.keys()
        )

        if candidate:
            return candidate[0]

        return None
