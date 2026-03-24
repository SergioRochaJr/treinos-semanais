"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def ex5(limit: int) -> int:
    """Find the largest prime factor of a given number.

    Args:
        limit (int): The number to find the largest prime factor for.

    Returns:
        int: The largest prime factor of the input number.
    """
    largest_factor: int = 1
    for i in range(2, int(limit**0.5) + 1):
        while limit % i == 0:
            largest_factor = i
            limit //= i
    if limit > 1:
        largest_factor = limit
    return largest_factor
