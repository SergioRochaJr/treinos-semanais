"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 == 91 X 99 .

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def ex7() -> int:
    """Find the largest palindrome made from the product of two 3-digit numbers.

    Returns:
        The largest palindromic number that is a product of two 3-digit numbers.
    """
    highest_palindrome = 9009
    for a in range(100, 1000):
        for b in range(100, 1000):
            product = a * b
            if product > highest_palindrome and str(product) == str(product)[::-1]:
                highest_palindrome = product
    return highest_palindrome
