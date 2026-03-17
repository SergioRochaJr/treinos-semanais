"""
The sum of the primes below 10 is 2+3+5+7 = 17.

Find the sum of all the primes below two million.
"""


def sum_primes_below(n: int) -> int:
    """
    Sums all prime numbers below the given number n.

    Args:
        n (int): The upper limit (exclusive) for summing primes.

    Returns:
        int: The sum of all primes less than n.
    """
    if n <= 2:
        return 0
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n : p] = [False] * len(range(p * p, n, p))

    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
