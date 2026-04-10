"""Domino chain solver using backtracking algorithm."""

from typing import List, Optional, Tuple

Domino = Tuple[int, int]
Chain = List[Domino]


def dominoes(pair: Chain) -> Optional[Chain]:
    """Find a valid domino chain arrangement if one exists.

    Args:
        pair (Chain): A list of dominoes to arrange.

    Returns:
        Optional[Chain]: A valid domino chain where each domino's right value matches
            the next domino's left value, and the chain forms a loop. Returns None
            if no valid arrangement exists.
    """
    if not pair:
        return []
    counts: dict[int, int] = {}
    for left, right in pair:
        counts[left] = counts.get(left, 0) + 1
        counts[right] = counts.get(right, 0) + 1
    for count in counts.values():
        if count % 2 != 0:
            return None

    def chain(current_chain: Chain, remaining: Chain) -> Optional[Chain]:
        """Recursively build a domino chain using backtracking.

        Args:
            current_chain (Chain): The chain built so far.
            remaining (Chain): The dominoes not yet used.

        Returns:
            Optional[Chain]: A valid complete chain if found, None otherwise.
        """
        if not remaining:
            first_number = current_chain[0][0]
            last_number = current_chain[-1][1]
            if first_number == last_number:
                return current_chain
            return None
        target = current_chain[-1][1]
        for i, (left, right) in enumerate(remaining):
            next_remaining = remaining[:i] + remaining[i + 1 :]
            if left == target:
                result = chain(current_chain + [(left, right)], next_remaining)
                if result:
                    return result
            if right == target:
                result = chain(current_chain + [(right, left)], next_remaining)
                if result:
                    return result

        return None

    return chain([pair[0]], pair[1:])
