"""
Instructions
Implement basic list operations.

In functional languages list operations like length, map, and reduce are very common. Implement a series of basic list operations, without using existing functions.

The precise number and names of the operations to be implemented will be track dependent to avoid conflicts with existing names, but the general operations you will implement include:

append (given two lists, add all items in the second list to the end of the first list);
concatenate (given a series of lists, combine all items in all lists into one flattened list);
filter (given a predicate and a list, return the list of all items for which predicate(item) is True);
length (given a list, return the total number of items within it);
map (given a function and a list, return the list of the results of applying function(item) on all items);
foldl (given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left);
foldr (given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right);
reverse (given a list, return a list with all the original items, but in reversed order).
Note, the ordering in which arguments are passed to the fold functions (foldl, foldr) is significant.
"""

from typing import Any


def append(a: list[Any], b: Any) -> list[Any]:
    """Append an item to the end of a list.

    Args:
        a: The list to append to.
        b: The item to append.

    Returns:
        The modified list with the item appended.
    """
    a[len(a) :] = [b]
    return a


def concatenate(series: list[list[Any]]) -> list[Any]:
    """Concatenate a series of lists into a single list.

    Args:
        series: A list of lists to concatenate.

    Returns:
        A single flattened list containing all items from the sublists.
    """
    return [item for sublist in series for item in sublist]


def filter(a: list[Any], target: Any) -> list[Any]:
    """Filter list to keep only items that match the target.

    Args:
        a: The list to filter.
        target: The value to match against.

    Returns:
        A new list containing only items that equal the target.
    """
    filtered_list: list[Any] = []
    for item in a:
        if item == target:
            append(filtered_list, item)
    return filtered_list


def length(a: list[Any]) -> int:
    """Get the length of a list.

    Args:
        a: The list to measure.

    Returns:
        The number of items in the list.
    """
    count = 0
    for _ in a:
        count += 1
    return count


def map(a: list[Any], func: Any) -> list[Any]:
    """Apply a function to each item in a list.

    Args:
        a: The list to map over.
        func: The function to apply to each item.

    Returns:
        A new list with the function applied to each original item.
    """
    mapped_list: list[Any] = []
    for item in a:
        append(mapped_list, func(item))
    return mapped_list


def foldl(initial_value: Any, a: list[Any], func: Any) -> Any:
    """Fold a list from the left (reduce with accumulator).

    Args:
        initial_value: The starting accumulator value.
        a: The list to fold over.
        func: The function to apply, taking (accumulator, item) and returning new accumulator.

    Returns:
        The final accumulator value after processing all items.
    """
    result = initial_value
    for item in a:
        result = func(result, item)
    return result


def foldr(initial_value: Any, a: list[Any], func: Any) -> Any:
    """Fold a list from the right (reduce with accumulator, right to left).

    Args:
        initial_value: The starting accumulator value.
        a: The list to fold over.
        func: The function to apply, taking (item, accumulator) and returning new accumulator.

    Returns:
        The final accumulator value after processing all items.
    """
    result = initial_value
    index = length(a) - 1
    while index >= 0:
        result = func(a[index], result)
        index -= 1
    return result


def reverse(a: list[Any]) -> list[Any]:
    """Reverse the order of items in a list.

    Args:
        a: The list to reverse.

    Returns:
        A new list with items in reverse order.
    """
    index = length(a) - 1
    new_list: list[Any] = []
    while index >= 0:
        new_list = append(new_list, a[index])
        index -= 1
    return new_list
