from typing import List

from .ingestor_interface import IngestorInterface, InvalidExtensionError
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .pdf_ingestor import PDFIngestor
from .txt_ingestor import TXTIngestor
from .quote_model import QuoteModel


class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise InvalidExtensionError
