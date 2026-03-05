"""
Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: nopqrstuvwxyzabcdefghijklm
It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.

Ciphertext is written out in the same formatting as the input including spaces and punctuation.

Examples
ROT5 omg gives trl
ROT0 c gives c
ROT26 Cool gives Cool
ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.
"""


class RotationalCipher:
    """A simple implementation of a rotational (Caesar) cipher.

    Attributes:
        key (int): The shift value used for encoding and decoding operations. It
            is always normalized to be within 0-25.
    """

    def __init__(self, key: int) -> None:
        """Initialize the cipher with a given key.

        Args:
            key (int): The rotation amount; can be any integer, positive or
                negative. It will be reduced modulo 26 to fit the alphabet.
        """
        self.key = key % 26

    def encode(self, key: int, message: str) -> str:
        """Return the input text shifted by ``key`` places in the alphabet.

        Non-alphabetic characters are preserved unchanged, and uppercase
        characters remain uppercase (same for lowercase).

        Args:
            key (int): rotation amount to apply; positive for forward shifts and
                negative for backward shifts. It is not normalized inside this
                method to allow callers to reuse the class key if desired.
            message (str): the plaintext to be encoded.

        Returns:
            str: the encoded ciphertext.
        """
        encoded_message: list[str] = []
        for char in message:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                encoded_char = chr((ord(char) - base + key) % 26 + base)
                encoded_message.append(encoded_char)
            else:
                encoded_message.append(char)
        return "".join(encoded_message)

    def decode(self, key: int, message: str) -> str:
        """Decode a message previously encoded with the provided key.

        This simply calls :meth:`encode` with the negated key.

        Args:
            key (int): the rotation that was originally used to encode the
                message.
            message (str): the ciphertext to decode.

        Returns:
            str: the decoded plaintext.
        """
        return self.encode(-key, message)

    def force_decode(self, message: str) -> list[str]:
        """Attempt to decode ``message`` using all possible keys.

        This is useful for brute-forcing a string when the key is unknown. It
        returns a list of all 26 candidate decodings, corresponding to keys 0–25.

        Args:
            message (str): the ciphertext for which to generate candidates.

        Returns:
            list[str]: all possible decodings.
        """
        return [self.decode(key, message) for key in range(26)]
