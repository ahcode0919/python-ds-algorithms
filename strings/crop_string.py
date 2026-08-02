def crop_string(string: str, new_length: int) -> str:
    """Crop String.

    Crop a string of words separated by spaces. Return the longest string possible without ending with whitespace
    or a partial word. Input will not start or end with spaces. If the rules cannot be met, return an empty string.

    Scan up to new_length, remembering the last space seen, and slice up to that point.
    """
    length = len(string)
    last_valid_index = 0

    if length <= new_length:
        return string

    for i in range(new_length):
        if string[i] == " ":
            last_valid_index = i

    return string[:last_valid_index]
