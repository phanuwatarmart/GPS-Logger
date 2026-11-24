"""
Logger Module

Save GPS records to a CSV log file.
"""

import csv

from config import LOG_FILE


def save_data(timestamp, latitude, longitude):
    """
    Save a GPS record to the CSV log file.

    Args:
        timestamp (str): Current date and time.
        latitude (float): GPS latitude.
        longitude (float): GPS longitude.
    """

    file_exists = LOG_FILE.exists()

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        # Create header if the file does not exist
        if not file_exists:
            writer.writerow(["Timestamp", "Latitude", "Longitude"])

        # Write GPS data
        writer.writerow([timestamp, latitude, longitude])