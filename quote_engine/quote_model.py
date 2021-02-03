class QuoteModel:
    def __init__(self, body, author):
        self._body = body
        self._author = author

    def __str__(self):
        return f'"{self._body}" - {self._author}'

    def __eq__(self, other):
        return self._body == other._body and self._author == other._author
