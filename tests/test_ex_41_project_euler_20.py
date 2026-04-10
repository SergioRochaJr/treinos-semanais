from training_exercises.ex_41_project_euler_20 import sum_digits_in_factorial


def test_factorial_10_example() -> None:
    assert sum_digits_in_factorial(10) == 27


def test_factorial_100_target() -> None:
    assert sum_digits_in_factorial(100) == 648


def test_factorial_0() -> None:
    assert sum_digits_in_factorial(0) == 1


def test_factorial_1() -> None:
    assert sum_digits_in_factorial(1) == 1
