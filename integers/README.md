# Integers

* [Fibonacci](#fibonacci)
* [Palindrome Number](#palindrome-number)
* [Reverse Number](#reverse-number)

## Fibonacci

A sequence that starts with `[0, 1]`. Each additional number is the sum of the last two numbers.

Example: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...]`

`fibonacci(5) -> 5`

```python
def fibonacci(number: int, memo: Dict[int, int] = None) -> int:
    if not memo:
        memo = {0: 0, 1: 1}

    if number not in memo:
        memo[number] = fibonacci(number - 1, memo) + fibonacci(number - 2, memo)

    return memo[number]


def fibonacci_with_array(number: int, memo=None) -> int:
    if memo is None:
        memo = [0, 1]

    if len(memo) > number:
        return memo[number]

    memo.append(memo[-1] + memo[-2])

    return fibonacci_with_array(number, memo)


@lru_cache(maxsize=None)
def fibonacci2(number: int) -> int:
    if number < 2:
        return number
    return fibonacci2(number - 1) + fibonacci2(number - 2)


def fibonacci3(number: int) -> int:
    if number == 0:
        return 0
    last_nbr: int = 0
    next_nbr: int = 1

    for _ in range(1, number):
        last_nbr, next_nbr = next_nbr, last_nbr + next_nbr

    return next_nbr


def fibonacci_sequence(number: int) -> Generator[int, None, None]:
    yield 0
    if number > 0:
        yield 1

    last_nbr: int = 0
    next_nbr: int = 1

    for _ in range(1, number):
        last_nbr, next_nbr = next_nbr, last_nbr + next_nbr
        yield next_nbr
```

## Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1: `121` -> `true`

Example 2: `-121` -> `false`

Explanation: From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

```python
def is_palindrome(x: int) -> bool:
    num = str(x)
    return num == num[::-1]
```

## Reverse Number

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: `123`

Output: `321`

```python
def reverse_number(number: int) -> int:
    reversed_number = int(str(abs(number))[::-1])

    if reversed_number > 2**31 - 1:  # Check for integer overflow (per question)
        return 0

    if number < 0:
        return -reversed_number
    return reversed_number
```
