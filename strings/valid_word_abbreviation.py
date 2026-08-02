"""Valid Word Abbreviation.

Given a non-empty word and an abbreviation, return whether the string matches the given abbreviation.

A string such as "word" contains only the following valid abbreviations: `["word", "1ord", "w1rd", "wo1d",
"wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]`. Notice that only the above
abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note: assume the word contains only lowercase letters, and the abbreviation contains only lowercase letters and
digits.

Example: `word = "internationalization"`, `abbr = "i12iz4n"` -> `True`
Example: `word = "apple"`, `abbr = "a2e"` -> `False`
"""


def valid_word_abbreviation(word: str, abbr: str) -> bool:
    """Walk the abbreviation, matching literal letters against word and skipping runs per numeric groups."""
    num = ""
    abbr_index = 0
    word_index = 0
    abbr_length = len(abbr)
    length = len(word)

    while abbr_index < abbr_length:
        if num.startswith("0"):
            return False
        if abbr[abbr_index].isalpha():
            if len(num) != 0:
                word_index += int(num)
                num = ""
            if word_index >= length or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1
        else:
            num += abbr[abbr_index]
            abbr_index += 1

    if len(num) > 0:
        return length == word_index + int(num)

    return True
