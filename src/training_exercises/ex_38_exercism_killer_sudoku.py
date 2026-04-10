"""
 Instructions

A friend of yours is learning how to solve Killer Sudokus (rules below) but struggling to figure out which digits can go in a cage. They ask you to help them out by writing a small program that lists all valid combinations for a given cage, and any constraints that affect the cage.

To make the output of your program easy to read, the combinations it returns must be sorted.

Killer Sudoku Rules

Standard Sudoku rules apply.

The digits in a cage, usually marked by a dotted line, add up to the small number given in the corner of the cage.

A digit may only occur once in a cage.

For a more detailed explanation, check out this guide.

Example 1: Cage with only 1 possible combination

In a 3-digit cage with a sum of 7, there is only one valid combination: 124.

1 + 2 + 4 = 7

Any other combination that adds up to 7, e.g. 232, would violate the rule of not repeating digits within a cage.


Example 2: Cage with several combinations

In a 2-digit cage with a sum 10, there are 4 possible combinations:

19

28

37

46


Example 3: Cage with several combinations that is restricted

In a 2-digit cage with a sum 10, where the column already contains a 1 and a 4, there are 2 possible combinations:

28

37

19 and 46 are not possible due to the 1 and 4 in the column according to standard Sudoku rules.


Trying it yourself

If you want to give an approachable Killer Sudoku a go, you can try out this puzzle by Clover, featured by Mark Goodliffe on Cracking The Cryptic on the 21st of June 2021.

You can also find Killer Sudokus in varying difficulty in numerous newspapers, as well as Sudoku apps, books and websites.

Credit

The screenshots above have been generated using F-Puzzles.com, a Puzzle Setting Tool by Eric Fox.
"""


def killer_sudoku(
    target: int, size: int, exclude: list[int] | None = None
) -> list[list[int]]:
    """Return all valid combinations for a Killer Sudoku cage.

    Args:
        target: The sum that the digits in the cage must reach.
        size: The number of digits required in the cage.
        exclude: Optional digits that cannot be used in the cage because they
            already appear in the same row, column, or block.

    Returns:
        A list of sorted digit combinations that sum to the target and contain
        no duplicate digits.
    """
    if exclude is None:
        exclude = []

    available_digits = [d for d in range(1, 10) if d not in exclude]
    valid_combinations: list[list[int]] = []

    def find_combos(
        start_index: int, current_combo: list[int], current_sum: int
    ) -> None:
        if len(current_combo) == size:
            if current_sum == target:
                valid_combinations.append(list(current_combo))
            return

        for i in range(start_index, len(available_digits)):
            current_combo.append(available_digits[i])
            find_combos(i + 1, current_combo, current_sum + available_digits[i])
            current_combo.pop()

    find_combos(0, [], 0)
    return valid_combinations
