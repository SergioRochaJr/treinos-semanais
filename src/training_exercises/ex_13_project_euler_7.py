"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from math import log


def ex13(n: int) -> int:
    """
    Find the nth prime number using the Sieve of Eratosthenes.

    For small values (n < 6), uses a lookup table. For larger values, generates
    primes up to an upper bound estimated by Rosser's theorem, then returns the
    nth prime.

    Args:
        n: The position of the prime number to find (1-indexed).

    Returns:
        The nth prime number.
    """
    if n < 6:
        return [2, 3, 5, 7, 11][n - 1]
    limit = int(n * (log(n) + log(log(n))))
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = [False] * len(range(p * p, limit + 1, p))
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes[n - 1]
