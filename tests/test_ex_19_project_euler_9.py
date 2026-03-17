from training_exercises.ex_19_project_euler_9 import pythagorean_triplet


def test_ex19() -> None:
    assert pythagorean_triplet(1000) == "200 * 375 * 425 = 31875000"


def test_ex19_no_triplet() -> None:
    assert pythagorean_triplet(10) == "No Pythagorean triplet found"
