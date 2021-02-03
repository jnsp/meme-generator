import pytest

from quote_engine import QuoteModel, CSVIngestor, InvalidExtensionError


class TestQuoteModel:
    def test_quote_model_str(self):
        body = 'This is a test quote'
        author = 'tester'
        test_quote = QuoteModel(body, author)
        assert str(test_quote) == f'"{body}" - {author}'


class TestCSVIngestor:
    def test_can_ingest(self):
        test_path = 'TEST_FILE.csv'
        assert CSVIngestor.can_ingest(test_path) is True

    def test_raise_exception_with_wrong_extension(self):
        test_path = 'TEST_FILE.txt'

        assert CSVIngestor.can_ingest(test_path) is False
        with pytest.raises(InvalidExtensionError):
            CSVIngestor.parse(test_path)

    def test_parse(self):
        test_path = './_data/SimpleLines/SimpleLines.csv'
        expected = [
            QuoteModel('Line 1', 'Author 1'),
            QuoteModel('Line 2', 'Author 2'),
            QuoteModel('Line 3', 'Author 3'),
            QuoteModel('Line 4', 'Author 4'),
            QuoteModel('Line 5', 'Author 5'),
        ]
        assert CSVIngestor.parse(test_path) == expected
