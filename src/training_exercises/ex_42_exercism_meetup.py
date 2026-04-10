from calendar import monthcalendar
from datetime import date


class MeetupDayException(ValueError):
    """Custom exception raised when an invalid meetup day is specified."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    """Calculate the date of a meetup based on the given parameters.

    Args:
        year (int): The year of the meetup.
        month (int): The month of the meetup.
        week (str): The week descriptor ('first', 'second', etc., 'teenth', 'last').
        day_of_week (str): The day of the week ('Monday', 'Tuesday', etc.).

    Returns:
        date: The calculated meetup date.

    Raises:
        MeetupDayException: If the week descriptor is invalid or the day does not exist.
    """
    day_mapping = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }
    target_weekday = day_mapping[day_of_week]
    cal = monthcalendar(year, month)

    valid_days = [
        week_data[target_weekday] for week_data in cal if week_data[target_weekday] != 0
    ]

    if week == "teenth":
        for day in valid_days:
            if 13 <= day <= 19:
                return date(year, month, day)
        raise AssertionError("Every month has a teenth day.")

    elif week == "last":
        return date(year, month, valid_days[-1])

    else:
        index_mapping = {
            "first": 0,
            "1st": 0,
            "second": 1,
            "2nd": 1,
            "third": 2,
            "3rd": 2,
            "fourth": 3,
            "4th": 3,
            "fifth": 4,
            "5th": 4,
        }

        index = index_mapping.get(week)

        if index is None:
            raise MeetupDayException("Invalid week descriptor.")

        if index >= len(valid_days):
            raise MeetupDayException("That day does not exist.")

        return date(year, month, valid_days[index])
