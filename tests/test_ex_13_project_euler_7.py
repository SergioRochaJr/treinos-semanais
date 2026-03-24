from pytest import mark

from training_exercises.ex_13_project_euler_7 import ex13


@mark.parametrize(
    "n, expected",
    [
        (1, 2),
        (2, 3),
        (6, 13),
        (10, 29),
        (10_001, 104_743),
    ],
)
def test_ex13(
    n: int,
    expected: int,
) -> None:
    assert ex13(n) == expected
