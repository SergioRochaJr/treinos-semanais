"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def ex11(n: int) -> int:
    """Calculate the difference between the square of sum and sum of squares.

    Computes (sum of first n natural numbers)^2 - (sum of squares of first n natural numbers)
    using the mathematical formulas:
    - Sum of first n natural numbers: n(n+1)/2
    - Sum of squares of first n natural numbers: n(n+1)(2n+1)/6

    Args:
        n: The upper limit (inclusive) of natural numbers to consider.

    Returns:
        The difference between the square of the sum and the sum of the squares.
    """
    return (((n * (n + 1)) // 2) ** 2) - (n * (n + 1) * (2 * n + 1)) // 6
