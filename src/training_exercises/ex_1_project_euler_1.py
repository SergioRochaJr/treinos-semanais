"""
If we list all the natural numbers below 10 that are multiples of 3
or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def exe1(limit: int) -> int:
    """
    Calculates the sum of all multiples of 3 or 5 below the given limit.

    Args:
        limit (int): The upper limit (exclusive) for the multiples.

    Returns:
        int: The sum of the multiples.
    """
    return sum(n for n in range(limit) if n % 3 == 0 or n % 5 == 0)
