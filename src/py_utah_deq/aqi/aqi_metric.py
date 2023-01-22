from dataclasses import dataclass
from datetime import datetime

from src.py_utah_deq.aqi.qualitative_metrics import MetricDescription


@dataclass
class AQIMetric:
    ozone: float
    ozone_level: MetricDescription
    ozone_8hr: float
    ozone_8hr_level: MetricDescription
    pm25: float
    pm25_level: MetricDescription
    pm25_24hr: float
    pm25_24hr_level: MetricDescription
    nox: float
    no2: float
    co: float
    timestamp: datetime
