from training_exercises.ex_16_exercism_diamond import diamond


def test_diamond() -> None:
    assert diamond("A") == "A\n"
    assert (
        diamond("D")
        == "   A   \n  B B  \n C   C \nD     D\n C   C \n  B B  \n   A   \n"
    )
