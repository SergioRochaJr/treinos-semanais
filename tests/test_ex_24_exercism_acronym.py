from pytest import mark

from training_exercises.ex_24_exercism_acronym import generate_acronym


@mark.parametrize(
    "phrase, expected",
    [
        ("Hello World!", "HW"),
        ("As Soon As Possible", "ASAP"),
        ("Liquid-crystal display", "LCD"),
        ("Thank George It's Friday!", "TGIF"),
    ],
)
def test_generate_acronym(
    phrase: str,
    expected: str,
) -> None:
    assert generate_acronym(phrase) == expected
