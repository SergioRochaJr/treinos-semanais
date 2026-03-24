"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce
from math import gcd


def smallest_divisible(limit: int) -> int:
    """Find the smallest positive number divisible by all numbers from 1 to limit.

    Uses brute force approach, iterating from limit upwards by limit increments.

    Args:
        limit: The upper bound for divisibility check (inclusive).

    Returns:
        The smallest positive number evenly divisible by all numbers from 1 to limit.
    """
    n = limit
    while True:
        if all(n % i == 0 for i in range(1, limit + 1)):
            return n
        n += limit


def smallest_divisible_math(limit: int) -> int:
    """Find the smallest positive number divisible by all numbers from 1 to limit.

    Uses the Least Common Multiple (LCM) approach via the GCD formula.
    Efficient mathematical solution.

    Args:
        limit: The upper bound for divisibility check (inclusive).

    Returns:
        The smallest positive number evenly divisible by all numbers from 1 to limit.
    """
    return reduce(lambda a, b: (a * b) // gcd(a, b), range(1, limit + 1))
