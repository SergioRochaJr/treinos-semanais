"""
Your task is to determine the date and time one gigasecond after a certain date.

A gigasecond is one thousand million seconds. That is a one with nine zeros after it.

If you were born on January 24th, 2015 at 22:00 (10:00:00pm), then you would be a gigasecond old on October 2nd, 2046 at 23:46:40 (11:46:40pm).
"""

from datetime import datetime, timedelta


def after_gigasecond(date: str) -> str:
    """Calculate the date and time one gigasecond after the given date.

    Args:
        date: A date and time string in the format "DD-MM-YYYYTHH:MM:SS" (ISO 8601 with dashes).

    Returns:
        The date and time string (in "DD-MM-YYYYTHH:MM:SS" format) representing the exact moment
        one gigasecond (10^9 seconds = ~31.7 years) after the input date and time.
    """
    input_date = datetime.strptime(date, "%d-%m-%YT%H:%M:%S")
    gigasecond = timedelta(seconds=10**9)
    result_date = input_date + gigasecond
    return result_date.strftime("%d-%m-%YT%H:%M:%S")
