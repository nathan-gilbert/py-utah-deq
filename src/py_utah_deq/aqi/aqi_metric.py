"""
Module for Air Quality data
"""
from dataclasses import dataclass
from datetime import datetime

from src.py_utah_deq.aqi.qualitative_metrics import MetricDescription


#pylint: disable=too-many-instance-attributes
@dataclass
class AQIMetric:
    """
    Data class for Air Quality Metrics
    """
    ozone: float
    ozone_level: MetricDescription
    ozone_8hr: float
    ozone_8hr_level: MetricDescription
    pm25: float
    pm25_level: MetricDescription
    pm25_24hr: float
    pm25_24hr_level: MetricDescription
    nitrogen_oxide: float
    nitrogen_dioxide: float
    carbon_monoxide: float
    timestamp: datetime
