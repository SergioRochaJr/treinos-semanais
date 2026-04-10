from training_exercises.ex_39_project_euler_19 import count_sundays_on_first


def test_twentieth_century_sundays() -> None:
    assert count_sundays_on_first(1901, 2000) == 171


def test_year_1900_sundays() -> None:
    assert count_sundays_on_first(1900, 1900) == 2


def test_leap_century_year() -> None:
    assert count_sundays_on_first(2000, 2000) == 1


def test_recent_leap_year() -> None:
    assert count_sundays_on_first(2024, 2024) == 2
