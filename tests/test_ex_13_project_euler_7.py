from training_exercises.ex_13_project_euler_7 import ex13


def test_ex13() -> None:
    assert ex13(1) == 2
    assert ex13(2) == 3
    assert ex13(6) == 13
    assert ex13(10) == 29
    assert ex13(10001) == 104743
