from typing import List, Optional

from training_exercises.ex_46_exercism_domino import Domino, dominoes


def is_valid_chain(
    original_tiles: List[Domino], result_chain: Optional[List[Domino]]
) -> bool:
    if not original_tiles:
        return result_chain == []
    if result_chain is None:
        return False
    if len(result_chain) != len(original_tiles):
        return False
    if result_chain[0][0] != result_chain[-1][1]:
        return False
    for i in range(len(result_chain) - 1):
        if result_chain[i][1] != result_chain[i + 1][0]:
            return False

    return True


def test_empty_input_empty_output() -> None:
    assert dominoes([]) == []


def test_singleton_input_valid() -> None:
    assert dominoes([(1, 1)]) == [(1, 1)]


def test_singleton_input_invalid() -> None:
    assert dominoes([(1, 2)]) is None


def test_three_elements() -> None:
    input_tiles = [(1, 2), (3, 1), (2, 3)]
    assert is_valid_chain(input_tiles, dominoes(input_tiles))


def test_three_elements_invalid() -> None:
    assert dominoes([(1, 2), (4, 1), (2, 3)]) is None


def test_can_reverse_dominoes() -> None:
    input_tiles = [(1, 2), (1, 3), (2, 3)]
    assert is_valid_chain(input_tiles, dominoes(input_tiles))


def test_need_backtrack() -> None:
    input_tiles = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
    assert is_valid_chain(input_tiles, dominoes(input_tiles))


def test_disconnected_islands() -> None:
    input_tiles = [(1, 2), (2, 1), (3, 4), (4, 3)]
    assert dominoes(input_tiles) is None
