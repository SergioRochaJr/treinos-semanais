from pytest import raises

from training_exercises.ex_40_exercism_tournament import tally


def test_just_the_header_if_no_input() -> None:
    expected = ["Team                           | MP |  W |  D |  L |  P"]
    assert tally([]) == expected


def test_a_win_is_three_points_a_loss_is_zero_points() -> None:
    results = ["Allegoric Alaskans;Blithering Badgers;win"]
    expected = [
        "Team                           | MP |  W |  D |  L |  P",
        "Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3",
        "Blithering Badgers             |  1 |  0 |  0 |  1 |  0",
    ]
    assert tally(results) == expected


def test_a_draw_is_one_point_each() -> None:
    results = ["Allegoric Alaskans;Blithering Badgers;draw"]
    expected = [
        "Team                           | MP |  W |  D |  L |  P",
        "Allegoric Alaskans             |  1 |  0 |  1 |  0 |  1",
        "Blithering Badgers             |  1 |  0 |  1 |  0 |  1",
    ]
    assert tally(results) == expected


def test_ties_broken_alphabetically() -> None:
    results = [
        "Courageous Californians;Allegoric Alaskans;win",
        "Devastating Donkeys;Blithering Badgers;win",
    ]
    expected = [
        "Team                           | MP |  W |  D |  L |  P",
        "Courageous Californians        |  1 |  1 |  0 |  0 |  3",
        "Devastating Donkeys            |  1 |  1 |  0 |  0 |  3",
        "Allegoric Alaskans             |  1 |  0 |  0 |  1 |  0",
        "Blithering Badgers             |  1 |  0 |  0 |  1 |  0",
    ]
    assert tally(results) == expected


def test_typical_input() -> None:
    results = [
        "Allegoric Alaskans;Blithering Badgers;win",
        "Devastating Donkeys;Courageous Californians;draw",
        "Devastating Donkeys;Allegoric Alaskans;win",
        "Courageous Californians;Blithering Badgers;loss",
        "Blithering Badgers;Devastating Donkeys;loss",
        "Allegoric Alaskans;Courageous Californians;win",
    ]
    expected = [
        "Team                           | MP |  W |  D |  L |  P",
        "Devastating Donkeys            |  3 |  2 |  1 |  0 |  7",
        "Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6",
        "Blithering Badgers             |  3 |  1 |  0 |  2 |  3",
        "Courageous Californians        |  3 |  0 |  1 |  2 |  1",
    ]
    assert tally(results) == expected


def test_ignore_empty_lines() -> None:
    results = [
        "Allegoric Alaskans;Blithering Badgers;win",
        "",
        "Devastating Donkeys;Courageous Californians;draw",
        "",
    ]
    expected = [
        "Team                           | MP |  W |  D |  L |  P",
        "Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3",
        "Courageous Californians        |  1 |  0 |  1 |  0 |  1",
        "Devastating Donkeys            |  1 |  0 |  1 |  0 |  1",
        "Blithering Badgers             |  1 |  0 |  0 |  1 |  0",
    ]
    assert tally(results) == expected


def test_invalid_match_result() -> None:
    results = ["Allegoric Alaskans;Blithering Badgers;cancelled"]
    with raises(ValueError, match="Resultado de partida inválido: cancelled"):
        tally(results)
