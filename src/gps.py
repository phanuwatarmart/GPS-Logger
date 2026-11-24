"""
GPS Module

Provide GPS coordinates using simulated data or a GPS receiver.
"""

import random

from config import (
    SIMULATION_MODE,
    SIMULATED_LATITUDE,
    SIMULATED_LONGITUDE,
    GPS_OFFSET,
)


def get_gps_data():
    """
    Return GPS coordinates.

    Returns:
        tuple[float, float]: Latitude and longitude coordinates.

    Raises:
        NotImplementedError: If hardware mode is selected but
            GPS support has not been implemented.
    """

    if SIMULATION_MODE:
        latitude = round(
            SIMULATED_LATITUDE + random.uniform(-GPS_OFFSET, GPS_OFFSET),
            6,
        )
        longitude = round(
            SIMULATED_LONGITUDE + random.uniform(-GPS_OFFSET, GPS_OFFSET),
            6,
        )

        return latitude, longitude

    raise NotImplementedError("Hardware mode is not implemented yet.")