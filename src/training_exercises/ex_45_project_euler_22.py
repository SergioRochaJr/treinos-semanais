def calculate_name_value(name: str) -> int:
    """Calculate the alphabetical value of a name.

    Args:
        name (str): The name to calculate the value for.

    Returns:
        int: The sum of the alphabetical positions of the letters in the name.
    """
    return sum(ord(char) - 64 for char in name.upper())


def total_name_scores(names: list[str]) -> int:
    """Calculate the total name scores for a list of names.

    Args:
        names (list[str]): The list of names.

    Returns:
        int: The total score.
    """
    sorted_names = sorted(names)
    total_score = 0
    for position, name in enumerate(sorted_names, start=1):
        name_value = calculate_name_value(name)
        total_score += name_value * position

    return total_score


def parse_file_content(content: str) -> list[str]:
    """Parse the file content into a list of names.

    Args:
        content (str): The content of the file as a string.

    Returns:
        list[str]: The list of parsed names.
    """
    if not content.strip():
        return []
    return [name.strip('"') for name in content.split(",")]
