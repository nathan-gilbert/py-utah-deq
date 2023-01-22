"""
Class for implementing a data source for Utah's Dept of Env Quality
"""
import csv
from datetime import datetime

import requests

from src.py_utah_deq.aqi.qualitative_metrics import ozone_qualitative_metrics, \
    pm25_qualitative_metrics
from src.py_utah_deq.aqi.aqi_metric import AQIMetric


class UtahDEQAPI:
    """
    Implementation Utah's DEQ AQI API
    """
    def __init__(self, feed_id: str = 'nr'):
        self.__feed_id = feed_id
        self.__api_url = f"https://air.utah.gov/csvFeed.php?id={self.__feed_id}"
        self.__timestamp_format = "%m/%d/%Y %H:%M:%S"

    @property
    def feed_id(self):
        return self.__feed_id

    @feed_id.setter
    def feed_id(self, new_feed_id: str):
        self.__feed_id = new_feed_id
        self.__api_url = f"https://air.utah.gov/csvFeed.php?id={self.__feed_id}"

    def get_current_aqi(self) -> AQIMetric:
        """

        :return:
        :rtype:
        """

        with requests.Session() as sesh:
            download = sesh.get(self.__api_url)
            decoded_content = download.content.decode('utf-8')

            reader = csv.DictReader(decoded_content.splitlines(),
                                    delimiter='\t')
            for row in reader:
                return AQIMetric(
                    ozone=float(row["ozone"]),
                    ozone_level=ozone_qualitative_metrics(
                        float(row["ozone"])),
                    ozone_8hr=float(row["ozone_8hr_avg"]),
                    ozone_8hr_level=ozone_qualitative_metrics(
                        (float(row["ozone_8hr_avg"]))),
                    pm25=float(row["pm25"]),
                    pm25_level=pm25_qualitative_metrics(float(row["pm25"])),
                    pm25_24hr=float(row["pm25_24hr_avg"]),
                    pm25_24hr_level=pm25_qualitative_metrics(
                        float(row["pm25_24hr_avg"])),
                    nox=float(row["nox"]),
                    no2=float(row["no2"]),
                    co=float(row["co"]),
                    timestamp=datetime.strptime(
                        row["dtstamp"],
                        self.__timestamp_format
                    )
                )
