from training_exercises.ex_21_project_euler_10 import sum_primes_below


def test_ex21() -> None:
    assert sum_primes_below(10) == 17
    assert sum_primes_below(2000000) == 142913828922
    assert sum_primes_below(2) == 0
    assert sum_primes_below(0) == 0
