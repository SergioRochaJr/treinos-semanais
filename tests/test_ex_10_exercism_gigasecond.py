from training_exercises.ex_10_exercism_gigasecond import after_gigasecond


def test_after_gigasecond() -> None:
    assert after_gigasecond("08-02-1994T00:00:00") == "17-10-2025T01:46:40"
