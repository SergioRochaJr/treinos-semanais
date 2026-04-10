"""
 You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,

April, June and November.

All the rest have thirty-one,

Saving February alone,

Which has twenty-eight, rain or shine.

And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date


def count_sundays_on_first(start_year: int, end_year: int) -> int:
    """Count how many Sundays fall on the first day of the month.

    Args:
        start_year: The first year to include in the range.
        end_year: The last year to include in the range.

    Returns:
        The number of months whose first day is a Sunday within the inclusive
        year range.
    """
    sunday_count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:
                sunday_count += 1

    return sunday_count
