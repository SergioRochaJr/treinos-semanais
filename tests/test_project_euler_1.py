from treinos_semanais.project_euler_1 import exe1


def test_example() -> None:
    assert 23 == exe1(10)


def test_wanted() -> None:
    assert 233_168 == exe1(1_000)
