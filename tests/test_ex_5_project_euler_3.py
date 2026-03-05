from training_exercises.ex_5_project_euler_3 import ex5


def test_wanted() -> None:
    assert 6_857 == ex5(600_851_475_143)


def test_small() -> None:
    assert 5 == ex5(10)
    assert 11 == ex5(33)
    assert 23 == ex5(46)
