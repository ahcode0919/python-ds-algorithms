def valid_parentheses(value: str) -> bool:
    if len(value) % 2 != 0:
        return False

    closing_values = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for char in value:
        if char in closing_values:
            stack.append(char)
        else:
            if not stack or closing_values[stack.pop()] != char:
                return False

    return len(stack) == 0
