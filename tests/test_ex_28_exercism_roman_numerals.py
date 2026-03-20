from pytest import raises

from training_exercises.ex_28_exercism_roman_numerals import roman_numeral


def test_roman_numerals() -> None:
    assert roman_numeral(3999) == "MMMCMXCIX"


def test_error() -> None:
    with raises(ValueError, match="Number should be higher than 0 and lower than 4000"):
        roman_numeral(40000)
