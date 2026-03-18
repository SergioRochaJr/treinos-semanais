from re import sub


def generate_acronym(phrase: str) -> str:
    sanitized_text = sub(r"[^a-zA-Z\s]", "", (phrase.replace("-", " ")))
    return "".join(word[0].upper() for word in sanitized_text.split())
