"""
The following iterative sequence is defined for the set of positive integers:
n->n/2 (n is even)
n->3n+1(n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.

It can be seen that this sequence (starting at 13 and finishing at 1) contains  terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def longest_collatz_sequence(limit: int) -> int:
    """
    Finds the starting number under the given limit that produces the longest Collatz sequence.

    Args:
        limit (int): The upper limit (exclusive) for starting numbers.

    Returns:
        int: The starting number with the longest sequence.
    """
    cache = {1: 1}
    max_length = 0
    longest_streak_number = 1

    for i in range(1, limit):
        n = i
        current_length = 0

        while n not in cache:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            current_length += 1

        total_length = current_length + cache[n]
        cache[i] = total_length

        if total_length > max_length:
            max_length = total_length
            longest_streak_number = i

    return longest_streak_number
