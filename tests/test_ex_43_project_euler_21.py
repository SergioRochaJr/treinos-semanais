from training_exercises.ex_43_project_euler_21 import d, sum_amicable_numbers


def test_d_example_220() -> None:
    assert d(220) == 284


def test_d_example_284() -> None:
    assert d(284) == 220


def test_d_prime_number() -> None:
    assert d(13) == 1


def test_d_less_than_two() -> None:
    assert d(1) == 0
    assert d(0) == 0


def test_perfect_number_is_not_amicable() -> None:
    assert sum_amicable_numbers(30) == 0


def test_project_euler_target() -> None:
    assert sum_amicable_numbers(10000) == 31626
