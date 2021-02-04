from typing import List
import subprocess
import os
import random

from .ingestor_interface import IngestorInterface, InvalidExtensionError
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidExtensionError

        tmp = f'./_data/{random.randint(0, 10000000)}.txt'

        try:
            subprocess.call(['pdftotext', path, tmp])
            quotes = list()

            with open(tmp, 'r') as f:
                for line in f:
                    if not (line := line.strip()):
                        continue

                    body, author = line.replace('"', '').split(' - ')
                    quote = QuoteModel(body, author)
                    quotes.append(quote)
        finally:
            os.remove(tmp)

        return quotes
