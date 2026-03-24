from training_exercises.ex_27_project_euler_13 import ten_digits


def test_ten_digits() -> None:
    assert (
        ten_digits([1_234_567_890_123_456_789, 1_000_000_009_123_456_789])
        == "2234567899"
    )
