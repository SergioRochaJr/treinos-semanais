from training_exercises.ex_34_exercism_simple_cipher import VigenereCipher


def test_random_key_generation() -> None:
    cipher = VigenereCipher()
    assert len(cipher.key) == 100
    assert cipher.key.isalpha()
    assert cipher.key.islower()


def test_encode_with_a_key() -> None:
    cipher = VigenereCipher("a")
    assert cipher.encode("hello") == "hello"


def test_encode_with_single_letter_key() -> None:
    cipher = VigenereCipher("d")
    assert cipher.encode("iamapandabear") == "ldpdsdqgdehdu"


def test_encode_with_multi_letter_key() -> None:
    cipher = VigenereCipher("abcd")
    assert cipher.encode("hello") == "hfnoo"


def test_decode_with_a_key() -> None:
    cipher = VigenereCipher("a")
    assert cipher.decode("hello") == "hello"


def test_decode_with_single_letter_key() -> None:
    cipher = VigenereCipher("d")
    assert cipher.decode("ldpdsdqgdehdu") == "iamapandabear"


def test_decode_with_multi_letter_key() -> None:
    cipher = VigenereCipher("abcd")
    assert cipher.decode("hfnoo") == "hello"


def test_encode_and_decode_symmetry_with_punctuation() -> None:
    cipher = VigenereCipher("python")
    plaintext = "hello, world! 123"
    encoded = cipher.encode(plaintext)
    decoded = cipher.decode(encoded)
    assert encoded != plaintext
    assert decoded == plaintext
