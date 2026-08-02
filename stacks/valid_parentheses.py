"""Valid Parentheses.

Given a string containing just the characters `(`, `)`, `{`, `}`, `[`, and `]`, determine if the input string is
valid. An input string is valid if open brackets are closed by the same type of bracket and closed in the correct
order. An empty string is also considered valid.

Example: `"()[]{}"` -> `True`
Example: `"(]"` -> `False`
"""


def valid_parentheses(value: str) -> bool:
    """Push opening brackets onto a stack and match each closing bracket against the top of the stack."""
    if len(value) % 2 != 0:
        return False

    closing_values = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for char in value:
        if char in closing_values:
            stack.append(char)
        else:
            if not stack or closing_values[stack.pop()] != char:
                return False

    return len(stack) == 0
