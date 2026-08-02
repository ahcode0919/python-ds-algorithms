def find_max_consecutive_ones_with_flip(nums: list[int]) -> int:
    """Find Max Consecutive Ones With One Flip.

    Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

    Example: `[1, 0, 1, 1, 0]` -> `4` (flipping the first zero yields a run of four consecutive 1s)

    Single pass tracking the most recent flipped zero to extend the current run.
    """
    zero = -1
    ones = 0
    highest = 0

    for index, num in enumerate(nums):
        if num == 1:
            ones += 1
        elif zero != -1:
            total = ones + 1
            if total > highest:
                highest = total
            ones = index - zero - 1
            zero = index
        else:
            zero = index

    last_total = ones

    if zero != -1:
        last_total += 1
    if last_total > highest:
        return last_total
    return highest
