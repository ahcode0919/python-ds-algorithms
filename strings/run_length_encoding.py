"""Run Length Encoding.

Perform run length encoding on an input string, replacing runs of repeated characters with the character followed
by its run length (omitting the length when it is 1).

Example: `"aaabbcddd"` -> `"a3b2cd3"`
"""


def run_length_encoding(string: str) -> str:
    """Walk the string counting consecutive repeats, flushing a character+count pair on each new character."""
    counter = 0
    current_character = None
    output = []

    for character in string:
        if current_character == character:
            counter += 1
        else:
            if current_character:
                output.append(current_character + str(counter if counter > 1 else ""))
            current_character = character
            counter = 1

    if current_character:
        output.append(current_character + str(counter if counter > 1 else ""))

    return "".join(output)
