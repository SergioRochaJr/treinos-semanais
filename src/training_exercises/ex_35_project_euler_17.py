"""
If the numbers  1 to 5  are written out in words: one, two, three, four, five, then there are    3 + 3 + 5 + 4 + 4 = 19   letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

from training_exercises.ex_22_exercism_say import say


def number_letter_count(n: int) -> int:
    """Count the total number of letters used when writing numbers 1 to n in words.
    
    Converts each number from 1 to n into its word representation and counts all
    letters (excluding spaces and hyphens) used across all numbers.
    
    Args:
        n: The upper limit (inclusive) of numbers to convert to words.
    
    Returns:
        The total count of letters used when writing all numbers from 1 to n.
    
    Example:
        number_letter_count(5) returns 19 because "one" + "two" + "three" + 
        "four" + "five" = 3 + 3 + 5 + 4 + 4 = 19 letters.
    """
    total_char = 0

    for i in range(1, n + 1):
        text = say(i)
        clean_text = text.replace(" ", "").replace("-", "")
        letters = len(clean_text)
        if i > 100 and i % 100 != 0:
            letters += 3

        total_char += letters

    return total_char
