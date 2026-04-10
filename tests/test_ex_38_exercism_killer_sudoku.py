from training_exercises.ex_38_exercism_killer_sudoku import killer_sudoku


def test_single_combination() -> None:
    assert killer_sudoku(7, 3) == [[1, 2, 4]]


def test_multiple_combinations() -> None:
    assert killer_sudoku(10, 2) == [[1, 9], [2, 8], [3, 7], [4, 6]]


def test_restricted_combinations() -> None:
    assert killer_sudoku(10, 2, exclude=[1, 4]) == [[2, 8], [3, 7]]


def test_one_digit_cage() -> None:
    assert killer_sudoku(5, 1) == [[5]]


def test_impossible_target() -> None:
    assert killer_sudoku(99, 2) == []


def test_all_useful_digits_excluded() -> None:
    assert killer_sudoku(3, 2, exclude=[1, 2]) == []


def test_no_exclude_parameter_provided() -> None:
    assert killer_sudoku(3, 2) == [[1, 2]]
