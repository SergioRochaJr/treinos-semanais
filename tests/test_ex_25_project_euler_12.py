from training_exercises.ex_25_project_euler_12 import triangle_divisors


def test_triangle_divisor() -> None:
    assert triangle_divisors(500) == 76576500
    assert triangle_divisors(5) == 28
