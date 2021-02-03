from typing import List
import csv

from .ingestor_interface import IngestorInterface, InvalidExtensionError
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidExtensionError

        quotes = list()
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                quote = QuoteModel(**row)
                quotes.append(quote)

        return quotes
