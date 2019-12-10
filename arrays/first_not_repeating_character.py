# Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you
# would be asked to do during a real interview.
#
# Given a string s, find and return the first instance of a non-repeating character in it.
# If there is no such character, return '_'.


def first_not_repeating_character(s: str) -> str:
    length = len(s)
    index = 0
    while index < length:
        if s[index] not in s[:index] and s[index] not in s[index + 1:]:
            return s[index]
        index += 1
    return '_'


def first_not_repeating_character_set(s: str) -> str:
    checked_characters = set()  # skip characters we've already checked.
    for char in s:
        if char not in checked_characters and s.index(char) == s.rindex(char):
            return char
        checked_characters.add(char)
    return '_'
