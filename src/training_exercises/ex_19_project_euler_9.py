"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

For example, 3^2 + 4^2 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplet(abc: int) -> str:
    """
    Finds the Pythagorean triplet where a + b + c = abc and returns the product abc as a string.

    Args:
        abc (int): The sum of the triplet.

    Returns:
        str: The product of the triplet or a message if not found.
    """
    a = 0
    b = 0
    c = 0
    for a in range(1, abc):
        for b in range(a, abc - a):
            c = abc - a - b
            if a**2 + b**2 == c**2:
                return f"{a} * {b} * {c} = {a * b * c}"
    return "No Pythagorean triplet found"
