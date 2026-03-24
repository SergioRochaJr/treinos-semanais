from pytest import mark

from training_exercises.ex_21_project_euler_10 import sum_primes_below


@mark.parametrize(
    "limit, expected",
    [
        (10, 17),
        (2_000_000, 142_913_828_922),
        (2, 0),
        (0, 0),
    ],
)
def test_ex21(
    limit: int,
    expected: int,
) -> None:
    assert sum_primes_below(limit) == expected
