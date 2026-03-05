"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 25; it is also an odd square.

The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35.

Among the first 605 thousand square numbers, what is the sum of all the odd squares?
"""


def ex0(odd_square: int) -> int:
    """Return the sum of odd square numbers up to the given value.

    This function computes the sum of the squares of all odd positive
    integers from 1 through ``odd_square`` (inclusive, if ``odd_square``
    itself is odd). It mirrors the Project Euler problem described in the
    module docstring: calculating the sum of odd square numbers within a
    certain range.

    Args:
        odd_square (int): upper bound for the odd integers to square.
            Only odd numbers in ``range(1, odd_square + 1, 2)`` are
            considered.

    Returns:
        int: the sum of the odd squares.
    """
    return sum(n**2 for n in range(1, odd_square + 1, 2))
