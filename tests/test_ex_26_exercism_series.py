from pytest import mark, raises

from training_exercises.ex_26_exercism_series import slices


@mark.parametrize(
    "series, length, expected",
    [
        ("49142", 3, ["491", "914", "142"]),
        ("49142", 4, ["4914", "9142"]),
        ("12345", 5, ["12345"]),
        (
            "5431235432131",
            3,
            [
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
            ],
        ),
    ],
)
def test_slices(
    series: str,
    length: int,
    expected: list[str],
) -> None:
    assert slices(series, length) == expected


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
