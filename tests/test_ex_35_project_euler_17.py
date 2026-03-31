from training_exercises.ex_35_project_euler_17 import number_letter_count


def test_number_letter_count_one() -> None:
    assert number_letter_count(1) == 3


def test_number_letter_count_example() -> None:
    assert number_letter_count(5) == 19


def test_number_letter_count_project_euler() -> None:
    assert number_letter_count(1000) == 21124
