from typing import List


def group_anagrams(strings: List[str]) -> List[List[str]]:
    """Group Anagrams.

    Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase, typically using all the original letters exactly once.

    Bucket strings by their sorted-character key, since anagrams share the same sorted form.
    """
    sorted_strings = ["".join(sorted(string)) for string in strings]
    answer = {}

    for index, value in enumerate(strings):
        if sorted_strings[index] in answer:
            answer[sorted_strings[index]].append(value)
        else:
            answer[sorted_strings[index]] = [value]
    return list(answer.values())
