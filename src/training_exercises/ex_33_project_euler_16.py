"""
2^15 = 32768  and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def power_sum(n: int, e: int) -> int:
    """
    Calculate the sum of digits in n raised to the power e.
    
    Args:
        n: The base number to be raised to a power.
        e: The exponent to raise n to.
    
    Returns:
        The sum of all digits in the result of n**e.
    
    Example:
        power_sum(2, 15) returns 26 because 2^15 = 32768 and 3+2+7+6+8 = 26.
    """
    return sum(int(digit) for digit in str(n**e))
