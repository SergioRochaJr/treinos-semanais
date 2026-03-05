from training_exercises.ex_4_exercism_rotational_cypher import RotationalCipher


def test_encode_rot13() -> None:
    cipher = RotationalCipher(13)
    expected = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
    assert expected == cipher.encode(13, "The quick brown fox jumps over the lazy dog.")


def test_decode_rot13() -> None:
    cipher = RotationalCipher(13)
    expected = "The quick brown fox jumps over the lazy dog."
    assert expected == cipher.decode(13, "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")


def test_force_decode_rot13() -> None:
    cipher = RotationalCipher(13)
    results = cipher.force_decode("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")
    assert len(results) == 26
    assert "The quick brown fox jumps over the lazy dog." in results
