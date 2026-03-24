from pytest import mark

from training_exercises.ex_16_exercism_diamond import diamond


@mark.parametrize(
    "letter, expected",
    [
        ("A", "A\n"),
        (
            "D",
            "   A   \n  B B  \n C   C \nD     D\n C   C \n  B B  \n   A   \n",
        ),
    ],
)
def test_diamond(
    letter: str,
    expected: str,
) -> None:
    assert diamond(letter) == expected
