from quote_engine import QuoteModel


class TestQuoteModel:
    def test_quote_model(self):
        body = 'This is a test quote'
        author = 'tester'
        test_quote = QuoteModel(body, author)
        assert str(test_quote) == f'"{body}" - {author}'
