"""
Project Configuration

Centralize application configuration values used throughout
the GPS Logger project, including logging, GPS, RTC,
and simulation settings.
"""

from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Project Mode
SIMULATION_MODE = True

# Logging
LOG_FILE = BASE_DIR / "sample_data" / "gps_log.csv"
LOG_INTERVAL = 5

# GPS Settings
GPS_PORT = "/dev/serial0"
GPS_BAUDRATE = 9600

# RTC Settings
RTC_I2C_ADDRESS = 0x68

# Simulation Settings
SIMULATION_MODE = True
SIMULATED_LATITUDE = 13.7563
SIMULATED_LONGITUDE = 100.5018
GPS_OFFSET = 0.01