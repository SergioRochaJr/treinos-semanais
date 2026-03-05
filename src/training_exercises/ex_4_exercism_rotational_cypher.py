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
    def __init__(self, key: int) -> None:
        self.key = key % 26

    def encode(self, key: int, message: str) -> str:
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
        return self.encode(-key, message)

    def force_decode(self, message: str) -> list[str]:
        return [self.decode(key, message) for key in range(26)]


print(RotationalCipher(13).encode(13, "The quick brown fox jumps over the lazy dog."))

print(RotationalCipher(13).decode(13, "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."))

print(RotationalCipher(13).force_decode("Gur dhvpx oebja sbk whzcf bire gur ynml qbt."))
