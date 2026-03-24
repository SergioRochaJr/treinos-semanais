from math import e, isclose, pi
from typing import Any

from pytest import mark

from training_exercises.ex_17_exercism_complex_numbers import ComplexNumber


@mark.parametrize(
    "c, expected",
    [
        (ComplexNumber(1, 2), ComplexNumber(1, -2)),
    ],
)
def test_conjugate(
    c: ComplexNumber,
    expected: ComplexNumber,
) -> None:
    assert c.conjugate() == expected


@mark.parametrize(
    "c, expected",
    [
        (ComplexNumber(3, 4), 5.0),
    ],
)
def test_absolute_value(
    c: ComplexNumber,
    expected: float,
) -> None:
    assert isclose(c.absolute_value(), expected)


@mark.parametrize(
    "c1, c2, expected",
    [
        (ComplexNumber(1, 2), ComplexNumber(3, 4), ComplexNumber(4, 6)),
    ],
)
def test_addition(
    c1: ComplexNumber,
    c2: ComplexNumber,
    expected: ComplexNumber,
) -> None:
    assert c1.addition(c2) == expected


@mark.parametrize(
    "c1, c2, expected",
    [
        (ComplexNumber(5, 5), ComplexNumber(2, 3), ComplexNumber(3, 2)),
    ],
)
def test_subtraction(
    c1: ComplexNumber,
    c2: ComplexNumber,
    expected: ComplexNumber,
) -> None:
    assert c1.subtraction(c2) == expected


@mark.parametrize(
    "c1, c2, expected",
    [
        (ComplexNumber(1, 2), ComplexNumber(3, 4), ComplexNumber(-5, 10)),
    ],
)
def test_multiplication(
    c1: ComplexNumber,
    c2: ComplexNumber,
    expected: ComplexNumber,
) -> None:
    assert c1.multiplication(c2) == expected


@mark.parametrize(
    "c, expected",
    [
        (ComplexNumber(1, 2), ComplexNumber(0.2, -0.4)),
    ],
)
def test_reciprocal(
    c: ComplexNumber,
    expected: ComplexNumber,
) -> None:
    assert c.reciprocal() == expected


@mark.parametrize(
    "c1, c2, expected",
    [
        (ComplexNumber(1, 2), ComplexNumber(3, 4), ComplexNumber(0.44, 0.08)),
    ],
)
def test_division(
    c1: ComplexNumber,
    c2: ComplexNumber,
    expected: ComplexNumber,
) -> None:
    assert c1.division(c2) == expected


@mark.parametrize(
    "c, expected",
    [
        (ComplexNumber(0, pi), ComplexNumber(-1.0, 0.0)),
        (ComplexNumber(1, 0), ComplexNumber(e, 0.0)),
    ],
)
def test_exponential(
    c: ComplexNumber,
    expected: ComplexNumber,
) -> None:
    assert c.exponential() == expected


@mark.parametrize(
    "c, other",
    [
        (ComplexNumber(1, 2), 5),
        (ComplexNumber(1, 2), "1, 2"),
        (ComplexNumber(1, 2), object()),
    ],
)
def test_eq_different_type(
    c: ComplexNumber,
    other: Any,
) -> None:
    assert c != other


@mark.parametrize(
    "c, expected",
    [
        (ComplexNumber(1, 2), "1, 2"),
        (ComplexNumber(-3.5, 4.0), "-3.5, 4.0"),
        (ComplexNumber(0, 0), "0, 0"),
    ],
)
def test_repr(
    c: ComplexNumber,
    expected: str,
) -> None:
    assert repr(c) == expected
