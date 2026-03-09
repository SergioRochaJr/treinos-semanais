from training_exercises.ex_9_project_euler_5 import (
    smallest_divisible,
    smallest_divisible_math,
)


def test_smallest_divisible() -> None:
    assert smallest_divisible(20) == 232_792_560


def test_smallest_divisible_math() -> None:
    assert smallest_divisible_math(20) == 232_792_560
