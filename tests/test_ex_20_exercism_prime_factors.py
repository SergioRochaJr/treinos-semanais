from training_exercises.ex_20_exercism_prime_factors import prime_factors


def test_prime_factors() -> None:
    assert prime_factors(0) == [0]
    assert prime_factors(1) == []
    assert prime_factors(2) == [2]
    assert prime_factors(8) == [2, 2, 2]
    assert prime_factors(9) == [3, 3]
    assert prime_factors(12) == [2, 2, 3]
