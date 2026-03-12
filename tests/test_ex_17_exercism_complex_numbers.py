import math

from training_exercises.ex_17_exercism_complex_numbers import ComplexNumber


def test_conjugate() -> None:
    assert ComplexNumber(1, 2).conjugate() == ComplexNumber(1, -2)


def test_absolute_value() -> None:
    assert math.isclose(ComplexNumber(3, 4).absolute_value(), 5.0)


def test_addition() -> None:
    assert ComplexNumber(1, 2).addition(ComplexNumber(3, 4)) == ComplexNumber(4, 6)


def test_subtraction() -> None:
    assert ComplexNumber(5, 5).subtraction(ComplexNumber(2, 3)) == ComplexNumber(3, 2)


def test_multiplication() -> None:
    assert ComplexNumber(1, 2).multiplication(ComplexNumber(3, 4)) == ComplexNumber(
        -5, 10
    )


def test_reciprocal() -> None:
    assert ComplexNumber(1, 2).reciprocal() == ComplexNumber(0.2, -0.4)


def test_division() -> None:
    assert ComplexNumber(1, 2).division(ComplexNumber(3, 4)) == ComplexNumber(
        0.44, 0.08
    )


def test_exponential() -> None:
    assert ComplexNumber(0, math.pi).exponential() == ComplexNumber(-1.0, 0.0)
    assert ComplexNumber(1, 0).exponential() == ComplexNumber(math.e, 0.0)


def test_eq_different_type() -> None:
    assert ComplexNumber(1, 2) != 5
    assert ComplexNumber(1, 2) != "1, 2"
    assert ComplexNumber(1, 2) != object()
