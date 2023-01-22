"""
Data source base class
"""
from abc import ABC, abstractmethod
from typing import Any


class DataSource(ABC):
    """Base Class for Data Source"""

    @abstractmethod
    def get_current_aqi(self) -> Any:
        raise NotImplementedError
