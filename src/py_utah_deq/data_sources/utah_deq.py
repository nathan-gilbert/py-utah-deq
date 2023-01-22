"""
Class for implementing a data source for Utah's Dept of Env Quality
"""
import csv
from typing import Any

import requests

from src.py_utah_deq.data_sources.data_source import DataSource


class UtahDEQ(DataSource):
    """
    Implementation of a DataSource from Utah's DEQ
    """
    def __init__(self):
        self.__api_url = 'https://air.utah.gov/csvFeed.php?id=nr'

    def get_current_aqi(self) -> Any:
        """

        :return:
        :rtype:
        """
        with requests.Session() as sesh:
            download = sesh.get(self.__api_url)
            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            for r in cr:
                print(r)
