from typing import List, Optional


def reverse_string(string: str) -> str:
    return string[::-1]


def reverse_string_with_list_comprehension(string: str) -> str:
    return ''.join([string[i] for i in range(len(string) - 1, -1, -1)])


def reverse_string_with_loop(string: str) -> str:
    reversed_str: List[Optional[str]] = [None] * len(string)
    for index in range(len(string) - 1, -1, -1):
        reversed_str[len(string) - 1 - index] = string[index]
    return ''.join(reversed_str)
