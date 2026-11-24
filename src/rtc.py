"""
RTC Module

Provide the current date and time for the application using
simulation or hardware mode.
"""

from datetime import datetime

from config import SIMULATION_MODE


def get_current_time():
    """
    Return the current date and time as a formatted string.

    Returns:
        str: Current date and time in YYYY-MM-DD HH:MM:SS format.

    Raises:
        NotImplementedError: If hardware mode is selected but
            RTC support has not been implemented.
    """

    if SIMULATION_MODE:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Hardware Mode
    # Will read from DS3231 later
    raise NotImplementedError(
        "Hardware mode is not implemented yet."
    )