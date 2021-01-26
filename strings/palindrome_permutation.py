from collections import Counter


def palindrome_permutation(palindrome: str) -> bool:
    length = len(palindrome)
    counter = Counter([char for char in palindrome])

    if length % 2 == 0:
        for key in counter:
            if counter[key] % 2 != 0:
                return False
    else:
        ones_count = Counter(counter.values()).get(1)
        if ones_count > 1:
            return False

    return True
