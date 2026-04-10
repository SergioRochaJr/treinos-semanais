from datetime import date
from typing import List

from pytest import MonkeyPatch, raises

from training_exercises.ex_42_exercism_meetup import MeetupDayException, meetup


def test_monteenth_of_may_2013() -> None:
    assert meetup(2013, 5, "teenth", "Monday") == date(2013, 5, 13)


def test_saturteenth_of_february_2013() -> None:
    assert meetup(2013, 2, "teenth", "Saturday") == date(2013, 2, 16)


def test_first_monday_of_march_2013() -> None:
    assert meetup(2013, 3, "first", "Monday") == date(2013, 3, 4)


def test_second_monday_of_march_2013() -> None:
    assert meetup(2013, 3, "second", "Monday") == date(2013, 3, 11)


def test_third_tuesday_of_may_2013() -> None:
    assert meetup(2013, 5, "third", "Tuesday") == date(2013, 5, 21)


def test_fourth_sunday_of_july_2013() -> None:
    assert meetup(2013, 7, "fourth", "Sunday") == date(2013, 7, 28)


def test_last_monday_of_march_2013() -> None:
    assert meetup(2013, 3, "last", "Monday") == date(2013, 3, 25)


def test_last_sunday_of_february_2012_leap_year() -> None:
    assert meetup(2012, 2, "last", "Sunday") == date(2012, 2, 26)


def test_fifth_thursday_of_may_2013() -> None:
    assert meetup(2013, 5, "fifth", "Thursday") == date(2013, 5, 30)


def test_non_existent_fifth_monday_of_february_2013() -> None:
    with raises(MeetupDayException, match="That day does not exist."):
        meetup(2013, 2, "fifth", "Monday")


def test_invalid_week_descriptor() -> None:
    with raises(MeetupDayException, match="Invalid week descriptor."):
        meetup(2013, 1, "invalid", "Monday")


def test_fifth_monday_of_march_2013_using_short_descriptor() -> None:
    assert meetup(2013, 3, "4th", "Monday") == date(2013, 3, 25)


def test_impossible_teenth_day_assertion(monkeypatch: MonkeyPatch) -> None:
    fake_calendar: List[List[int]] = [[0] * 7 for _ in range(5)]

    def mock_monthcalendar(_year: int, _month: int) -> List[List[int]]:
        return fake_calendar

    monkeypatch.setattr(
        "training_exercises.ex_42_exercism_meetup.monthcalendar", mock_monthcalendar
    )

    with raises(AssertionError, match="Every month has a teenth day."):
        meetup(2024, 1, "teenth", "Monday")
