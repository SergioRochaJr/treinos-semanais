from math import isqrt


def d(n: int) -> int:
    """Calculate the sum of proper divisors of n.

    Args:
        n (int): The number to find divisors for.

    Returns:
        int: The sum of proper divisors.
    """
    if n <= 1:
        return 0

    divisor_sum = 1
    limit = isqrt(n)

    for i in range(2, limit + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i

    return divisor_sum


def sum_amicable_numbers(limit: int) -> int:
    """Calculate the sum of all amicable numbers below the given limit.

    Args:
        limit (int): The upper limit (exclusive) for finding amicable numbers.

    Returns:
        int: The sum of amicable numbers below the limit.
    """
    amicable_sum = 0

    for a in range(2, limit):
        b = d(a)
        if a != b and d(b) == a:
            amicable_sum += a

    return amicable_sum
