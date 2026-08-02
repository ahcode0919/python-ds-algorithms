def count_primes(number: int) -> int:
    """Count Primes.

    Count the number of prime numbers less than a non-negative number.

    Example: `Input: 10` -> `Output: 4`
    """
    is_prime = [True] * number

    for num in range(2, number):
        if not num * num < number:
            break
        if not is_prime[num]:
            continue

        num1 = num * num
        while num1 < number:
            is_prime[num1] = False
            num1 += num

    count = 0
    for index in range(2, number):
        if is_prime[index]:
            count += 1
    return count
