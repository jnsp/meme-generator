from typing import List
from pdfminer.high_level import extract_text

from .ingestor_interface import IngestorInterface, InvalidExtensionError
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidExtensionError

        quotes = list()
        extracted = extract_text(path).replace('"', '')
        tokens = [s.strip() for s in extracted.split('\n')]
        for token in tokens:
            if not token:
                continue

            body, author = token.split(' - ')
            quote = QuoteModel(body, author)
            quotes.append(quote)

        return quotes
