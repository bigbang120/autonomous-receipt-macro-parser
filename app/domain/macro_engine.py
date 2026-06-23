from app.domain.nutrition_db import MACROS
from app.domain.item_matcher import ItemMatcher


class MacroEngine:

    def calculate(
        self,
        items
    ):

        matcher = ItemMatcher()

        output = []

        totals = {
            "calories":0,
            "protein":0,
            "carbs":0,
            "fat":0
        }

        for item in items:

            match = matcher.match(
                item
            )

            if not match:
                continue

            data = MACROS[match]

            output.append({
                "item": match,
                **data
            })

            for k in totals:
                totals[k] += data[k]

        return {
            "items": output,
            "totals": totals
        }
