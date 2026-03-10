from training_exercises.ex_12_exercism_pig_latim import pig_latim_encoder


def test_pig_latin_encoder() -> None:

    assert pig_latim_encoder("apple") == "appleay"
    assert pig_latim_encoder("xray") == "xrayay"
    assert pig_latim_encoder("yttria") == "yttriaay"
    assert pig_latim_encoder("chair") == "airchay"
    assert pig_latim_encoder("square") == "aresquay"
    assert pig_latim_encoder("rhythm") == "ythmrhay"
    assert pig_latim_encoder("") == ""
