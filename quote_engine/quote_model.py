class QuoteModel:
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        return f'"{self.body}" - {self.author}'

    def __eq__(self, other):
        return self.body == other.body and self.author == other.author
