from training_exercises.ex_14_exercism_matching_brackets import matching_brackets


def test_matching_brackets() -> None:
    assert matching_brackets("This is a test (with some [brackets] in it).") is True
    assert matching_brackets("This is a test (with some [brackets in it).") is False
    assert matching_brackets("This is a test (with some brackets] in it).") is False
    assert matching_brackets("This is a test with some brackets in it).") is False
    assert matching_brackets("This is a test with some (brackets in it).") is True
