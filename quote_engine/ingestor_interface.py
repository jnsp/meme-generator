from abc import ABC, abstractmethod
from typing import List

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
