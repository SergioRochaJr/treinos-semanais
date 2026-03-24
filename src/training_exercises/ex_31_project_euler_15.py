"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

from math import comb


def lattice_paths(grid_h: int, grid_w: int) -> int:
    """
    Calculates the number of lattice paths from the top-left to the bottom-right
    of a grid, moving only right and down.

    Args:
        grid_h (int): The height of the grid (number of down moves).
        grid_w (int): The width of the grid (number of right moves).

    Returns:
        int: The number of possible paths.
    """
    return comb(grid_h + grid_w, grid_w)
