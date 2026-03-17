"""
Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.

Note that 1 is not a prime number.

Example
What are the prime factors of 60?

Our first divisor is 2. 2 goes into 60, leaving 30.
2 goes into 30, leaving 15.
2 doesn't go cleanly into 15. So let's move on to our next divisor, 3.
3 goes cleanly into 15, leaving 5.
3 does not go cleanly into 5. The next possible factor is 4.
4 does not go cleanly into 5. The next possible factor is 5.
5 does go cleanly into 5.
We're left only with 1, so now, we're done.
Our successful divisors in that computation represent the list of prime factors of 60: 2, 2, 3, and 5.

You can check this yourself:

2 * 2 * 3 * 5
= 4 * 15
= 60
Success!
"""


def prime_factors(n: int) -> list[int]:
    """
    Computes the prime factors of a given natural number.

    Args:
        n (int): The number to factorize. If n is 0, returns [0].

    Returns:
        list[int]: The list of prime factors in ascending order.
    """
    if n == 0:
        return [0]
    factors: list[int] = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors
