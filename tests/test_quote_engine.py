import pytest

from quote_engine import QuoteModel, CSVIngestor, DOCXIngestor, \
    PDFIngestor, TXTIngestor, Ingestor, InvalidExtensionError


def test_quote_model_str():
    body = 'This is a test quote'
    author = 'tester'
    test_quote = QuoteModel(body, author)
    assert test_quote._body
    assert test_quote._author
    assert str(test_quote) == f'"{body}" - {author}'


@pytest.mark.parametrize('test_ingestor, right_exts',
                         [(CSVIngestor, ['csv']),
                          (DOCXIngestor, ['docx']),
                          (PDFIngestor, ['pdf']),
                          (TXTIngestor, ['txt']),
                          (Ingestor, ['csv', 'docx', 'pdf', 'txt'])],
                         ids=lambda l: str(l) if isinstance(l, list) else None)
class TestIngestor:
    def test_can_ingest(self, test_ingestor, right_exts):
        if test_ingestor != Ingestor:
            right_file = 'TEST_FILE.' + right_exts[0]
            assert test_ingestor.can_ingest(right_file) is True

    def test_raise_exception(self, test_ingestor, right_exts):
        wrong_file = 'TEST_FILE.' + 'wrong_ext'
        assert test_ingestor.can_ingest(wrong_file) is False
        with pytest.raises(InvalidExtensionError):
            test_ingestor.parse(wrong_file)

    def test_parse(self, test_ingestor, right_exts):
        expected = [
            QuoteModel('Line 1', 'Author 1'),
            QuoteModel('Line 2', 'Author 2'),
            QuoteModel('Line 3', 'Author 3'),
            QuoteModel('Line 4', 'Author 4'),
            QuoteModel('Line 5', 'Author 5'),
        ]
        for right_ext in right_exts:
            test_path = './_data/SimpleLines/SimpleLines.' + right_ext
            assert test_ingestor.parse(test_path) == expected
