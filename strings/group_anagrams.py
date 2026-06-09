from typing import List


def group_anagrams(strings: List[str]) -> List[List[str]]:
    sorted_strings = ["".join(sorted(string)) for string in strings]
    answer = {}

    for index, value in enumerate(strings):
        if sorted_strings[index] in answer:
            answer[sorted_strings[index]].append(value)
        else:
            answer[sorted_strings[index]] = [value]
    return list(answer.values())
