from math import isclose
from typing import Any

from pytest import mark, raises

from training_exercises.ex_18_exercism_rational_number import RationalNumber


@mark.parametrize(
    "r, expected",
    [
        (RationalNumber(2, 4), RationalNumber(1, 2)),
        (RationalNumber(-4, 6), RationalNumber(-2, 3)),
        (RationalNumber(3, -4), RationalNumber(-3, 4)),
    ],
)
def test_reduction(
    r: RationalNumber,
    expected: RationalNumber,
) -> None:
    assert r == expected


@mark.parametrize(
    "r, expected",
    [
        (RationalNumber(-1, 2), RationalNumber(1, 2)),
        (RationalNumber(3, -4), RationalNumber(3, 4)),
    ],
)
def test_absolute_value(
    r: RationalNumber,
    expected: RationalNumber,
) -> None:
    assert r.absolute_value() == expected


@mark.parametrize(
    "r1, r2, expected",
    [
        (RationalNumber(1, 2), RationalNumber(2, 3), RationalNumber(7, 6)),
    ],
)
def test_sum(
    r1: RationalNumber,
    r2: RationalNumber,
    expected: RationalNumber,
) -> None:
    assert r1.sum(r2) == expected


@mark.parametrize(
    "r1, r2, expected",
    [
        (RationalNumber(1, 2), RationalNumber(2, 3), RationalNumber(-1, 6)),
    ],
)
def test_difference(
    r1: RationalNumber,
    r2: RationalNumber,
    expected: RationalNumber,
) -> None:
    assert r1.difference(r2) == expected


@mark.parametrize(
    "r1, r2, expected",
    [
        (RationalNumber(1, 2), RationalNumber(2, 3), RationalNumber(1, 3)),
    ],
)
def test_product(
    r1: RationalNumber,
    r2: RationalNumber,
    expected: RationalNumber,
) -> None:
    assert r1.product(r2) == expected


@mark.parametrize(
    "r1, r2, expected",
    [
        (RationalNumber(1, 2), RationalNumber(2, 3), RationalNumber(3, 4)),
    ],
)
def test_divide(
    r1: RationalNumber,
    r2: RationalNumber,
    expected: RationalNumber,
) -> None:
    assert r1.divide(r2) == expected


@mark.parametrize(
    "r, power, expected",
    [
        (RationalNumber(1, 2), 3, RationalNumber(1, 8)),
    ],
)
def test_exponentiate(
    r: RationalNumber,
    power: int,
    expected: RationalNumber,
) -> None:
    assert r.exponentiate(power) == expected


@mark.parametrize(
    "r, power, expected",
    [
        (RationalNumber(1, 2), -3, RationalNumber(8, 1)),
    ],
)
def test_negative_exponential(
    r: RationalNumber,
    power: int,
    expected: RationalNumber,
) -> None:
    assert r.negative_exponential(power) == expected


@mark.parametrize(
    "r, power, expected",
    [
        (RationalNumber(4, 9), 0.5, 0.6666666666666666),
    ],
)
def test_floating_point_exponentiation(
    r: RationalNumber,
    power: float,
    expected: float,
) -> None:
    assert isclose(r.floating_point_exponentiation(power), expected)


@mark.parametrize(
    "r, base, expected",
    [
        (RationalNumber(1, 2), 9.0, 3.0),
    ],
)
def test_exp_real_base(
    r: RationalNumber,
    base: float,
    expected: float,
) -> None:
    assert isclose(r.exp_real_base(base), expected)


@mark.parametrize(
    "r, other",
    [
        (RationalNumber(1, 2), 5),
        (RationalNumber(1, 2), "1/2"),
        (RationalNumber(1, 2), object()),
    ],
)
def test_eq_different_type(
    r: RationalNumber,
    other: Any,
) -> None:
    assert r != other


@mark.parametrize(
    "r, expected",
    [
        (RationalNumber(1, 2), "1/2"),
        (RationalNumber(-3, 4), "-3/4"),
        (RationalNumber(0, 5), "0/1"),
    ],
)
def test_str_representation(
    r: RationalNumber,
    expected: str,
) -> None:
    assert str(r) == expected


def test_negative_exponential_zero_raises_error() -> None:
    with raises(ValueError, match="Cannot raise zero to a negative power."):
        RationalNumber(0, 1).negative_exponential(-3)


def test_divide_by_zero_raises_error() -> None:
    with raises(ValueError, match="Cannot divide by zero."):
        RationalNumber(1, 2).divide(RationalNumber(0, 5))


def test_zero_denominator_raises_error() -> None:
    with raises(ValueError, match="Denominator cannot be zero."):
        RationalNumber(1, 0)
