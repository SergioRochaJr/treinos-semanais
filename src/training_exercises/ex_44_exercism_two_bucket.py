from collections import deque
from math import gcd
from typing import Tuple


def measure(
    bucket_one: int, bucket_two: int, goal: int, start_bucket: str
) -> Tuple[int, str, int]:
    """Solve the two bucket problem to reach the goal amount with minimum steps.

    Args:
        bucket_one (int): The capacity of the first bucket.
        bucket_two (int): The capacity of the second bucket.
        goal (int): The target amount to measure.
        start_bucket (str): The bucket to start filling ('one' or 'two').

    Returns:
        Tuple[int, str, int]: A tuple containing the number of steps, the bucket that contains the goal amount, and the amount in the other bucket.

    Raises:
        ValueError: If the goal is larger than both buckets, not achievable with the bucket sizes, invalid start_bucket, or goal cannot be reached.
    """
    if goal > max(bucket_one, bucket_two):
        raise ValueError("Goal is larger than both buckets.")
    if goal % gcd(bucket_one, bucket_two) != 0:
        raise ValueError("Goal is not achievable with these bucket sizes.")

    if start_bucket == "one":
        start_state = (bucket_one, 0)
        invalid_state = (
            0,
            bucket_two,
        )
    elif start_bucket == "two":
        start_state = (0, bucket_two)
        invalid_state = (bucket_one, 0)
    else:
        raise ValueError("start_bucket must be 'one' or 'two'")

    queue: deque[tuple[tuple[int, int], int]] = deque([(start_state, 1)])

    visited: set[tuple[int, int]] = set()
    visited.add(start_state)
    visited.add(invalid_state)

    while queue:
        (b1, b2), steps = queue.popleft()

        if b1 == goal:
            return (steps, "one", b2)
        if b2 == goal:
            return (steps, "two", b1)

        next_states = [
            (bucket_one, b2),
            (b1, bucket_two),
            (0, b2),
            (b1, 0),
            (b1 - min(b1, bucket_two - b2), b2 + min(b1, bucket_two - b2)),
            (b1 + min(b2, bucket_one - b1), b2 - min(b2, bucket_one - b1)),
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, steps + 1))

    raise ValueError("Goal cannot be reached.")
