from typing import List, Optional, Tuple

Domino = Tuple[int, int]
Chain = List[Domino]


def dominoes(pair: Chain) -> Optional[Chain]:
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
