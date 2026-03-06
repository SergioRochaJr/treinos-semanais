from training_exercises.ex_8_exercism_space_age import SpaceAge


def test_on_earth() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_earth() == 31.69


def test_on_mercury() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_mercury() == 131.57


def test_on_venus() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_venus() == 51.51


def test_on_mars() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_mars() == 16.85


def test_on_jupiter() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_jupiter() == 2.67


def test_on_saturn() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_saturn() == 1.08


def test_on_uranus() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_uranus() == 0.38


def test_on_neptune() -> None:
    age = SpaceAge(1_000_000_000)
    assert age.on_neptune() == 0.19
