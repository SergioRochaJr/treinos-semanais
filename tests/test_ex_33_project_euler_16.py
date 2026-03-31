from training_exercises.ex_33_project_euler_16 import power_sum


def test_power_sum_example() -> None:
    assert power_sum(2, 15) == 26


def test_power_sum_small_numbers() -> None:
    assert power_sum(2, 4) == 7


def test_power_sum_exponent_zero() -> None:
    assert power_sum(123, 0) == 1


def test_power_sum_base_zero() -> None:
    assert power_sum(0, 10) == 0


def test_power_sum_powers_of_ten() -> None:
    assert power_sum(10, 100) == 1


def test_power_sum_project_euler_16() -> None:
    assert power_sum(2, 1000) == 1366
