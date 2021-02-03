import pytest

from quote_engine import QuoteModel, CSVIngestor, DOCXIngestor, \
    InvalidExtensionError


class TestQuoteModel:
    def test_quote_model_str(self):
        body = 'This is a test quote'
        author = 'tester'
        test_quote = QuoteModel(body, author)
        assert str(test_quote) == f'"{body}" - {author}'


@pytest.mark.parametrize('test_ingestor, right_ext',
                         [(CSVIngestor, 'csv'), (DOCXIngestor, 'docx')])
class TestIngestor:
    def test_can_ingest(self, test_ingestor, right_ext):
        test_filename = 'TEST_FILE'

        right_file = test_filename + '.' + right_ext
        assert test_ingestor.can_ingest(right_file) is True

        wrong_file = test_filename + '.' + 'wrong_ext'
        assert test_ingestor.can_ingest(wrong_file) is False

        with pytest.raises(InvalidExtensionError):
            test_ingestor.parse(wrong_file)

    def test_parse(self, test_ingestor, right_ext):
        test_path = './_data/SimpleLines/SimpleLines.' + right_ext
        expected = [
            QuoteModel('Line 1', 'Author 1'),
            QuoteModel('Line 2', 'Author 2'),
            QuoteModel('Line 3', 'Author 3'),
            QuoteModel('Line 4', 'Author 4'),
            QuoteModel('Line 5', 'Author 5'),
        ]
        assert test_ingestor.parse(test_path) == expected
