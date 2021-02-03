from typing import List
import docx

from .ingestor_interface import IngestorInterface, InvalidExtensionError
from .quote_model import QuoteModel


class DOCXIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidExtensionError

        quotes = list()
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if not paragraph.text:
                continue

            body, author = paragraph.text.replace('"', '').split(' - ')
            quote = QuoteModel(body, author)
            quotes.append(quote)

        return quotes
