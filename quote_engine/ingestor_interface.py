from abc import ABC, abstractmethod
from typing import List

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    allowed_extentions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extention = path.split('.')[-1]
        return extention in cls.allowed_extentions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
