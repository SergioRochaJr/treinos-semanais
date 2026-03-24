from pytest import mark

from training_exercises.ex_20_exercism_prime_factors import prime_factors


@mark.parametrize(
    "number, expected",
    [
        (0, [0]),
        (1, []),
        (2, [2]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (12, [2, 2, 3]),
    ],
)
def test_prime_factors(
    number: int,
    expected: list[int],
) -> None:
    assert prime_factors(number) == expected
