"""

n! means n x (n - 1) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3_628_800,

and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""

from math import factorial


def sum_digits_in_factorial(n: int) -> int:
    """Return the sum of the digits in n!.

    Args:
        n: The integer whose factorial digit sum should be computed.

    Returns:
        The sum of the digits in the decimal representation of n!.
    """
    fact = factorial(n)
    digit_sum = sum(int(digit) for digit in str(fact))

    return digit_sum
