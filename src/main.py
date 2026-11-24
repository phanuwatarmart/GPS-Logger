"""
Main Program

Run the GPS Logger application.
"""

import time

from config import LOG_INTERVAL
from gps import get_gps_data
from logger import save_data
from rtc import get_current_time


def main():
    """
    Run the GPS Logger application.
    """
    print("=" * 50)
    print("GPS Logger Started")
    print("=" * 50)

    try:
        while True:
            # Read GPS
            latitude, longitude = get_gps_data()

            # Read time
            timestamp = get_current_time()

            # Save CSV
            save_data(timestamp, latitude, longitude)

            # Display result
            print(f"Time      : {timestamp}")
            print(f"Latitude  : {latitude}")
            print(f"Longitude : {longitude}")
            print("-" * 50)

            time.sleep(LOG_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopping GPS Logger...")
        print("Goodbye 👋")


if __name__ == "__main__":
    main()