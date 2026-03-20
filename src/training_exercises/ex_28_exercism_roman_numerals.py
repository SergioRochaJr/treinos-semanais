def roman_numeral(number: int) -> str:
    if number > 3999 or number <= 0:
        raise ValueError("Number should be higher than 0 and lower than 4000")
    roman_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    result = ""
    for value, numeral in roman_map.items():
        while number >= value:
            result += numeral
            number -= value
    return result
