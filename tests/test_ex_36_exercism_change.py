from pytest import raises

from training_exercises.ex_36_exercism_change import coin_change


def test_change_for_zero() -> None:
    assert coin_change([1, 5, 10, 25, 100], 0) == []


def test_single_coin_change() -> None:
    assert coin_change([1, 5, 10, 25, 100], 25) == [25]


def test_multiple_coin_change() -> None:
    assert coin_change([1, 5, 10, 25, 100], 15) == [5, 10]


def test_change_with_lilliputian_coins() -> None:
    assert coin_change([1, 3, 4], 6) == [3, 3]


def test_coin_holt_bakery_example() -> None:
    assert coin_change([2, 5, 10], 12) == [2, 10]


def test_cannot_make_target() -> None:
    with raises(ValueError, match="can't make target with given coins"):
        coin_change([5, 10], 3)


def test_cannot_make_target_even_with_large_coins() -> None:
    with raises(ValueError, match="can't make target with given coins"):
        coin_change([5, 10], 94)


def test_negative_target() -> None:
    with raises(ValueError, match="change can't be negative"):
        coin_change([1, 2, 5], -5)
