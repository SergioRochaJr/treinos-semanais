from pytest import mark

from training_exercises.ex_12_exercism_pig_latim import pig_latim_encoder


@mark.parametrize(
    "word, expected",
    [
        ("apple", "appleay"),
        ("xray", "xrayay"),
        ("yttria", "yttriaay"),
        ("chair", "airchay"),
        ("square", "aresquay"),
        ("rhythm", "ythmrhay"),
        ("", ""),
    ],
)
def test_pig_latin_encoder(
    word: str,
    expected: str,
) -> None:
    assert pig_latim_encoder(word) == expected
