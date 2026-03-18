from training_exercises.ex_22_exercism_say import say


def test_say() -> None:
    assert say(0) == "zero"
    assert say(1) == "one"
    assert say(14) == "fourteen"
    assert say(20) == "twenty"
    assert say(22) == "twenty-two"
    assert say(100) == "one hundred"
    assert (
        say(123_456_789_123)
        == "one hundred twenty-three billion four hundred fifty-six million seven hundred eighty-nine thousand one hundred twenty-three"
    )
    try:
        say(-1)
        AssertionError("Expected ValueError for negative input")
    except ValueError:
        pass
    try:
        say(1_000_000_000_000)
        AssertionError("Expected ValueError for input above 999,999,999,999")
    except ValueError:
        pass
