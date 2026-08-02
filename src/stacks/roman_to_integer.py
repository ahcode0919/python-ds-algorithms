ROMAN_NUMERALS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(roman: str) -> int:
    """Roman to Integer.

    Roman numerals are represented by seven different symbols: I (1), V (5), X (10), L (50), C (100), D (500), and
    M (1000). Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to
    3999.

    Scan right to left, subtracting a value from the accumulator when a smaller numeral precedes a larger one.

    Example: `"MCMXCIV"` -> `1994`
    """
    number = 0
    accumulator = []

    for index in range(len(roman) - 1, -1, -1):
        if accumulator and ROMAN_NUMERALS[accumulator[-1]] > ROMAN_NUMERALS[roman[index]]:
            number += ROMAN_NUMERALS[accumulator.pop()] - ROMAN_NUMERALS[roman[index]]
        else:
            accumulator.append(roman[index])
    while accumulator:
        number += ROMAN_NUMERALS[accumulator.pop()]

    return number
