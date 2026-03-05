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


"""
def map(): 
    pass


def foldl():
    pass


def foldr():
    pass


def reverse():
    pass
"""
