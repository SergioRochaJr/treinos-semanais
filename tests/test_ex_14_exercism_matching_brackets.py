from pytest import mark

from training_exercises.ex_14_exercism_matching_brackets import matching_brackets


@mark.parametrize(
    "text, expected",
    [
        ("This is a test (with some [brackets] in it).", True),
        ("This is a test (with some [brackets in it).", False),
        ("This is a test (with some brackets] in it).", False),
        ("This is a test with some brackets in it).", False),
        ("This is a test with some (brackets in it).", True),
    ],
)
def test_matching_brackets(
    text: str,
    expected: bool,
) -> None:
    assert matching_brackets(text) is expected
