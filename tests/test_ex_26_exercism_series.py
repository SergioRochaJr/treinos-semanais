from pytest import raises

from training_exercises.ex_26_exercism_series import slices


def test_slices() -> None:
    assert slices("49142", 3) == ["491", "914", "142"]
    assert slices("49142", 4) == ["4914", "9142"]
    assert slices("12345", 5) == ["12345"]
    expected_result = [
        "543",
        "431",
        "312",
        "123",
        "235",
        "354",
        "543",
        "432",
        "321",
        "213",
        "131",
    ]
    assert slices("5431235432131", 3) == expected_result


def test_slice_length_cannot_be_zero() -> None:
    with raises(ValueError, match="slice length cannot be zero"):
        slices("12345", 0)


def test_slice_length_cannot_be_negative() -> None:
    with raises(ValueError, match="slice length cannot be negative"):
        slices("123", -1)


def test_series_cannot_be_empty() -> None:
    with raises(ValueError, match="series cannot be empty"):
        slices("", 1)


def test_slice_length_cannot_be_greater_than_series_length() -> None:
    with raises(ValueError, match="slice length cannot be greater than series length"):
        slices("123", 4)
