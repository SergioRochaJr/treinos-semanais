from pytest import mark, raises

from training_exercises.ex_22_exercism_say import say


@mark.parametrize(
    "number, expected",
    [
        (0, "zero"),
        (1, "one"),
        (14, "fourteen"),
        (20, "twenty"),
        (22, "twenty-two"),
        (100, "one hundred"),
        (1_000, "one thousand"),
        (1_000_000, "one million"),
        (1_002_345, "one million two thousand three hundred forty-five"),
        (
            123_456_789_123,
            "one hundred twenty-three billion four hundred fifty-six million seven hundred eighty-nine thousand one hundred twenty-three",
        ),
    ],
)
def test_say(
    number: int,
    expected: str,
) -> None:
    assert say(number) == expected


def test_negative_number_raises_error() -> None:
    with raises(ValueError, match="Invalid order number"):
        say(-1)


def test_number_above_maximum_raises_error() -> None:
    with raises(ValueError, match="Invalid order number"):
        say(1_000_000_000_000)
