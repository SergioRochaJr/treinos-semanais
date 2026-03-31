from pytest import raises

from training_exercises.ex_32_exercism_hamming_distance import hamming_distance


def test_empty_strands() -> None:
    assert hamming_distance("", "") == 0


def test_single_letter_identical_strands() -> None:
    assert hamming_distance("A", "A") == 0


def test_single_letter_different_strands() -> None:
    assert hamming_distance("G", "T") == 1


def test_long_identical_strands() -> None:
    assert hamming_distance("GGACTGAAATCTG", "GGACTGAAATCTG") == 0


def test_long_different_strands() -> None:
    assert hamming_distance("GGACGGATTCTG", "AGGACGGATTCT") == 9


def test_example_from_instructions() -> None:
    assert hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7


def test_disallow_first_strand_longer() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        hamming_distance("AATG", "AAA")


def test_disallow_second_strand_longer() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        hamming_distance("ATA", "AGTG")


def test_disallow_empty_first_strand() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        hamming_distance("", "G")


def test_disallow_empty_second_strand() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        hamming_distance("G", "")
