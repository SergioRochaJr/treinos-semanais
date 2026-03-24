from training_exercises.ex_31_project_euler_15 import lattice_paths


def test_lattice_paths_small_squares() -> None:
    assert lattice_paths(2, 2) == 6
    assert lattice_paths(3, 3) == 20


def test_lattice_paths_rectangles() -> None:
    assert lattice_paths(20, 4) == 10626
    assert lattice_paths(4, 20) == 10626


def test_lattice_paths_project_euler() -> None:
    assert lattice_paths(20, 20) == 137846528820
