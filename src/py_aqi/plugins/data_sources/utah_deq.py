"""
Class for implementing a data source for Utah's Dept of Env Quality
"""
from typing import Any

from src.py_aqi.plugins.data_sources.data_source import DataSource


class UtahDEQ(DataSource):
    """
    Implementation of a DataSource from Utah's DEQ
    """

    def get_current_aqi(self) -> Any:
        pass
