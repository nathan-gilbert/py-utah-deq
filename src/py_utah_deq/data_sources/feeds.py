"""
Module for Feeds enum.
"""
from enum import Enum


class Feeds(Enum):
    """
    Feeds are AQI monitor locations.
    """
    SALT_LAKE = "slc"
    BOX_ELDER = "boxelder"
    CACHE = "sm"
    CARBON = "p2"
    DAVIS = "bv"
    DUCHESNE = "rs"
    IRON = "en"
    TOOELE = "tooele"
    UINTAH = "v4"
    UTAH = "ln"
    WASHINGTON = "washington"
    WEBER = "hv"
