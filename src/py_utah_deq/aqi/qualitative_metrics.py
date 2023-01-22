"""
Helper functions for generating qualitative metrics from AQI data
"""
from collections import namedtuple

MetricDescription = namedtuple('MetricDescription', ['long', 'short'])

GOOD = MetricDescription(long="Good", short="Good")
MODERATE = MetricDescription(long="Moderate", short="Moderate")
UNHEALTHY1 = MetricDescription(long="Unhealthy for sensitive groups",
                               short="Unhealthy 1")
UNHEALTHY2 = MetricDescription(long="Unhealthy 2",
                               short="Unhealthy 2")
UNHEALTHY3 = MetricDescription(long="Very Unhealthy",
                               short="Unhealthy 3")
HAZARDOUS = MetricDescription(long="Hazardous",
                               short="Hazardous")


def ozone_qualitative_metrics(ozone_level: float) -> MetricDescription:
    """
    Returns a qualitative description of the ozone reading provided.

    :param ozone_level: The ozone metric
    :type ozone_level: float
    :return: Textual description of current ozone level
    :rtype: MetricDescription
    """
    if ozone_level <= 0.054:
        return GOOD
    if 0.054 < ozone_level <= 0.070:
        return MODERATE
    if 0.070 < ozone_level <= 0.085:
        return UNHEALTHY1
    if 0.080 < ozone_level <= 0.105:
        return UNHEALTHY2
    if 0.105 < ozone_level <= 0.2:
        return UNHEALTHY3
    if ozone_level > 0.2:
        return HAZARDOUS


def pm25_qualitative_metrics(pm25_level: float) -> MetricDescription:
    """
    Returns a qualitative description of the PM2.5 reading provided.

    :param pm25_level: The pm25 metric
    :type pm25_level: float
    :return: Textual description of current ozone level
    :rtype: MetricDescription
    """
    if pm25_level <= 12.0:
        return GOOD
    if 12.0 < pm25_level <= 35.4:
        return MODERATE
    if 35.4 < pm25_level <= 55.4:
        return UNHEALTHY1
    if 55.4 < pm25_level <= 150.4:
        return UNHEALTHY2
    if 150.4 < pm25_level <= 250.4:
        return UNHEALTHY3
    if pm25_level > 250.4:
        return HAZARDOUS
