class ReceiptParser:

    def extract_items(
        self,
        text: str
    ):

        rows = text.splitlines()

        clean = []

        for r in rows:

            r = r.strip()

            if r:
                clean.append(r)

        return clean
