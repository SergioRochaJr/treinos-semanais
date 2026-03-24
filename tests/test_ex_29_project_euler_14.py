from training_exercises.ex_29_project_euler_14 import longest_collatz_sequence


def test_longest_collatz_sequence_small_limits() -> None:
    assert longest_collatz_sequence(10) == 9
    assert longest_collatz_sequence(6) == 3


def test_longest_collatz_sequence_large_limit() -> None:
    assert longest_collatz_sequence(1000000) == 837799
