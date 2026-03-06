from typing import Any


def append(a: list[Any], b: Any) -> list[Any]:
    a[len(a) :] = [b]
    return a


def concatenate(series: list[list[Any]]) -> list[Any]:
    return [item for sublist in series for item in sublist]


def filter(a: list[Any], target: Any) -> list[Any]:
    filtered_list: list[Any] = []
    for item in a:
        if item == target:
            append(filtered_list, item)
    return filtered_list


def length(a: list[Any]) -> int:
    count = 0
    for _ in a:
        count += 1
    return count


def map(a: list[Any], func: Any) -> list[Any]:
    mapped_list: list[Any] = []
    for item in a:
        append(mapped_list, func(item))
    return mapped_list


def foldl(initial_value: Any, a: list[Any], func: Any) -> Any:
    result = initial_value
    for item in a:
        result = func(result, item)
    return result


def foldr(initial_value: Any, a: list[Any], func: Any) -> Any:
    result = initial_value
    index = length(a) - 1
    while index >= 0:
        result = func(a[index], result)
        index -= 1
    return result


def reverse(a: list[Any]) -> list[Any]:
    index = length(a) - 1
    new_list: list[Any] = []
    while index >= 0:
        new_list = append(new_list, a[index])
        index -= 1
    return new_list
