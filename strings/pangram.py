def pangram(string: str) -> bool:
    """Pangram.

    Determine if a string has all characters a-z. Should handle uppercase, lowercase, whitespace, and special
    characters.

    Collect the lowercased set of alphabetic characters and check if all 26 letters are present.
    """
    alpha_set = set()

    for char in string:
        if char.isalpha():
            alpha_set.add(char.lower())

    return len(alpha_set) == 26
