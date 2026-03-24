from pytest import mark, raises

from training_exercises.ex_30_exercism_phone_number import PhoneNumber


@mark.parametrize(
    "dirty_number, expected_clean",
    [
        ("+1 (613)-995-0253", "6139950253"),
        ("613-995-0253", "6139950253"),
        ("1 613 995 0253", "6139950253"),
        ("613.995.0253", "6139950253"),
        ("(223) 456-7890", "2234567890"),
    ],
)
def test_phone_number_happy_paths(dirty_number: str, expected_clean: str) -> None:
    phone = PhoneNumber(dirty_number)
    assert phone.number == expected_clean
    assert phone.area_code == expected_clean[:3]


def test_phone_number_exceptions() -> None:
    with raises(ValueError, match="letters not permitted"):
        PhoneNumber("123-abc-7890")

    with raises(ValueError, match="punctuations not permitted"):
        PhoneNumber("123-@56-7890")

    with raises(ValueError, match="must not be fewer than 10 digits"):
        PhoneNumber("123456789")

    with raises(ValueError, match="must not be greater than 11 digits"):
        PhoneNumber("123456789012")

    with raises(ValueError, match="11 digits must start with 1"):
        PhoneNumber("22234567890")

    with raises(ValueError, match="area code cannot start with zero"):
        PhoneNumber("10234567890")

    with raises(ValueError, match="area code cannot start with one"):
        PhoneNumber("11234567890")

    with raises(ValueError, match="exchange code cannot start with zero"):
        PhoneNumber("2230567890")

    with raises(ValueError, match="exchange code cannot start with one"):
        PhoneNumber("2231567890")
