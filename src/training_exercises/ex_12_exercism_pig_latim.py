import re

"""
Your task is to translate text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants:

vowels: the letters a, e, i, o, and u
consonants: the other 21 letters of the English alphabet
Rule 1
If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

For example:

"apple" -> "appleay" (starts with vowel)
"xray" -> "xrayay" (starts with "xr")
"yttria" -> "yttriaay" (starts with "yt")
Rule 2
If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.

For example:

"pig" -> "igp" -> "igpay" (starts with single consonant)
"chair" -> "airch" -> "airchay" (starts with multiple consonants)
"thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
Rule 3
If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.

For example:

"quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
"square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")
Rule 4
If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

Some examples:

"my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
"rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")
"""


def pig_latim_encoder(word: str) -> str:
    """
    Convert an English word to Pig Latin.

    Transforms the input word by applying Pig Latin rules based on its initial
    vowel and consonant patterns.

    Args:
        word: The English word to convert to Pig Latin (case-insensitive).

    Returns:
        The word converted to Pig Latin.
    """
    word = word.lower()

    if re.match(r"^([aeiou]|xr|yt)", word):
        return word + "ay"

    if match := re.match(r"^([^aeiou]*qu)", word):
        prefix = match.group(1)
        return word[len(prefix) :] + prefix + "ay"

    if match := re.match(r"^([^aeiou]+)(y.*)", word):
        consonants = match.group(1)
        rest = match.group(2)
        return rest + consonants + "ay"

    if match := re.match(r"^([^aeiou]+)(.*)", word):
        consonants = match.group(1)
        rest = match.group(2)
        return rest + consonants + "ay"

    return word
