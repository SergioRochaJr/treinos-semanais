import math

from training_exercises.ex_18_exercism_rational_number import RationalNumber


def test_reduction() -> None:
    assert RationalNumber(2, 4) == RationalNumber(1, 2)
    assert RationalNumber(-4, 6) == RationalNumber(-2, 3)
    assert RationalNumber(3, -4) == RationalNumber(-3, 4)


def test_absolute_value() -> None:
    assert RationalNumber(-1, 2).absolute_value() == RationalNumber(1, 2)
    assert RationalNumber(3, -4).absolute_value() == RationalNumber(3, 4)


def test_sum() -> None:
    assert RationalNumber(1, 2).sum(RationalNumber(2, 3)) == RationalNumber(7, 6)


def test_difference() -> None:
    assert RationalNumber(1, 2).difference(RationalNumber(2, 3)) == RationalNumber(
        -1, 6
    )


def test_product() -> None:
    assert RationalNumber(1, 2).product(RationalNumber(2, 3)) == RationalNumber(1, 3)


def test_divide() -> None:
    assert RationalNumber(1, 2).divide(RationalNumber(2, 3)) == RationalNumber(3, 4)


def test_exponentiate() -> None:
    assert RationalNumber(1, 2).exponentiate(3) == RationalNumber(1, 8)


def test_negative_exponential() -> None:
    assert RationalNumber(1, 2).negative_exponential(-3) == RationalNumber(8, 1)


def test_floating_point_exponentiation() -> None:
    # Usamos math.isclose para comparar floats e evitar bugs de arredondamento
    assert math.isclose(
        RationalNumber(4, 9).floating_point_exponentiation(0.5), 0.6666666666666666
    )


def test_exp_real_base() -> None:
    assert math.isclose(RationalNumber(1, 2).exp_real_base(9.0), 3.0)


def test_eq_different_type() -> None:
    assert RationalNumber(1, 2) != 5
    assert RationalNumber(1, 2) != "1/2"
    assert RationalNumber(1, 2) != object()
