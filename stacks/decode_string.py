def decode_string(value: str) -> str:
    """Decode String.

    Given an encoded string, return its decoded string. The encoding rule is `k[encoded_string]`, where the
    encoded_string inside the square brackets is repeated exactly k times. k is guaranteed to be a positive integer.
    The input string is always valid: no extra whitespace, well-formed square brackets, and the original data does
    not contain digits (digits are only used for the repeat counts) -- there won't be input like `3a` or `2[4]`.

    Push characters onto a stack, and on each ']' pop back to the matching '[' and repeat count.

    Example: `3[a2[c]]` -> `accaccacc`
    """
    stack = []
    for char in value:
        if char != "]":
            stack.append(char)
        else:
            temp_string, num = "", ""
            while stack and stack[-1] != "[":
                temp_string = stack.pop() + temp_string

            stack.pop()
            while stack and stack[-1].isdigit():
                num = stack.pop() + num

            num = int(num)
            stack.append(temp_string * num)

    return "".join(stack)
