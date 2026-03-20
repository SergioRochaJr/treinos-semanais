from training_exercises.ex_27_project_euler_13 import ten_digits


def test_ten_digits() -> None:
    assert ten_digits([1234567890123456789, 1000000009123456789]) == "2234567899"
