from typing import List

from .ingestor_interface import IngestorInterface, InvalidExtensionError
from .quote_model import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidExtensionError

        quotes = list()
        with open(path, 'r') as f:
            for line in f:
                if not (line := line.strip()):
                    continue

                body, author = line.replace('"', '').split(' - ')
                quote = QuoteModel(body, author)
                quotes.append(quote)

        return quotes
