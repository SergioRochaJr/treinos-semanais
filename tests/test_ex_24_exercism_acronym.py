from training_exercises.ex_24_exercism_acronym import generate_acronym


def test_generate_acronym() -> None:
    assert generate_acronym("Hello World!") == "HW"
    assert generate_acronym("As Soon As Possible") == "ASAP"
    assert generate_acronym("Liquid-crystal display") == "LCD"
    assert generate_acronym("Thank George It's Friday!") == "TGIF"
