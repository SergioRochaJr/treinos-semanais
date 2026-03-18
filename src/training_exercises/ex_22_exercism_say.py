def say(n: int) -> str:
    """Convert a number to its English word representation.

    Args:
        n (int): The number to convert. Must be between 0 and 999,999,999,999 inclusive.

    Returns:
        str: The English word representation of the number.

    Raises:
        ValueError: If n is negative or greater than 999,999,999,999.
    """
    if n < 0 or n > 999_999_999_999:
        raise ValueError("Invalid order number")
    if n == 0:
        return "zero"

    unit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    thousands = ["", "thousand", "million", "billion"]

    def process_chunk(chunk_int: int) -> str:
        s: list[str] = []
        hundreds = chunk_int // 100
        remainder = chunk_int % 100

        if hundreds > 0:
            s.append(f"{unit[hundreds]} hundred")

        if remainder > 0:
            if 0 < remainder < 10:
                s.append(unit[remainder])
            elif 10 <= remainder < 20:
                s.append(teens[remainder - 10])
            else:
                t = tens[remainder // 10]
                u = unit[remainder % 10]
                s.append(f"{t}-{u}" if u else t)

        return " ".join(s)

    num_str = str(n)
    chunks: list[int] = []
    for i in range(len(num_str), 0, -3):
        start = max(0, i - 3)
        chunks.append(int(num_str[start:i]))
    final_words: list[str] = []
    for i in range(len(chunks)):
        if chunks[i] != 0:
            chunk_text = process_chunk(chunks[i])
            scale = thousands[i]
            if scale:
                final_words.append(f"{chunk_text} {scale}")
            else:
                final_words.append(chunk_text)

    return " ".join(reversed(final_words)).strip()
