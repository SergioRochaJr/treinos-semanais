"""
The diamond kata takes as its input a letter, and outputs it in a diamond shape. Given a letter, it prints a diamond starting with 'A', with the supplied letter at the widest point.

Requirements
The first row contains one 'A'.
The last row contains one 'A'.
All rows, except the first and last, have exactly two identical letters.
All rows have as many trailing spaces as leading spaces. (This might be 0).
The diamond is horizontally symmetric.
The diamond is vertically symmetric.
The diamond has a square shape (width equals height).
The letters form a diamond shape.
The top half has the letters in ascending order.
The bottom half has the letters in descending order.
The four corners (containing the spaces) are triangles.
"""


def diamond(letter: str) -> str:
    """Generate a diamond shape with letters.

    Creates a diamond pattern with the provided letter at the widest point.
    Starts from 'A' at the top, expands to the given letter in the middle,
    then contracts back to 'A' at the bottom. The diamond is symmetric both
    horizontally and vertically, with each row (except first and last)
    containing two identical letters separated by spaces.

    Args:
        letter: An uppercase or lowercase letter (A-Z) that defines the diamond's width.

    Returns:
        A string representing the diamond shape with newline-separated rows,
        ending with a trailing newline.
    """
    n = ord(letter) - ord("A")
    rows: list[str] = []
    for i in range(n + 1):
        char = chr(ord("A") + i)
        outer_padding = " " * (n - i)
        if char == "A":
            row = f"{outer_padding}A{outer_padding}"
        else:
            inner_padding = " " * (2 * i - 1)
            row = f"{outer_padding}{char}{inner_padding}{char}{outer_padding}"
        rows.append(row)
    full_diamond = rows + rows[:-1][::-1]
    return "\n".join(full_diamond) + "\n"
