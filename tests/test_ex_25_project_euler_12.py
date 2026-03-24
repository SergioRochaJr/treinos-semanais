from pytest import mark

from training_exercises.ex_25_project_euler_12 import triangle_divisors


@mark.parametrize(
    "n, expected",
    [
        (500, 76_576_500),
        (5, 28),
    ],
)
def test_triangle_divisor(
    n: int,
    expected: int,
) -> None:
    assert triangle_divisors(n) == expected
