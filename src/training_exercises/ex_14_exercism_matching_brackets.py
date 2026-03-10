def matching_brackets(code: str) -> bool:
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    stack: list[str] = []
    for char in code:
        if char in bracket_pairs:
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack or bracket_pairs[stack.pop()] != char:
                return False
    return not stack
