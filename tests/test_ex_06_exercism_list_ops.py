from training_exercises.ex_06_exercism_list_ops import (
    append,
    concatenate,
    filter,
    foldl,
    foldr,
    length,
    map,
    reverse,
)


def test_append() -> None:
    base_list = [1, 2]
    result: list[int] = append(base_list, 3)
    assert result == [1, 2, 3]
    assert base_list == [1, 2, 3]


def test_concatenate() -> None:
    series = [[1, 2], [3], [4, 5]]
    result: list[int] = concatenate(series)
    assert result == [1, 2, 3, 4, 5]


def test_filter() -> None:
    items = [10, 20, 10, 30]
    result: list[int] = filter(items, 10)
    assert result == [10, 10]


def test_length() -> None:
    items = ["a", "b", "c", "d"]
    result: int = length(items)
    assert result == 4


def test_map() -> None:
    items = [1, 2, 3]

    def double(x: int) -> int:
        return x * 2

    result: list[int] = map(items, double)
    assert result == [2, 4, 6]


def test_foldl() -> None:
    items = [1, 2, 3]

    def subtract(acc: int, item: int) -> int:
        return acc - item

    result: int = foldl(10, items, subtract)
    assert result == 4


def test_foldr() -> None:
    items = [1, 2, 3]

    def subtract(item: int, acc: int) -> int:
        return item - acc

    result: int = foldr(10, items, subtract)
    assert result == -8


def test_reverse() -> None:
    items = [1, 2, 3]
    result: list[int] = reverse(items)
    assert result == [3, 2, 1]
