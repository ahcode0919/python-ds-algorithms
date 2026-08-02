def minimum_subarray_length(target: int, numbers: list[int]) -> int:
    """Minimum Subarray Length.

    Find the minimal length of a contiguous subarray whose sum is greater than or equal to target. If there isn't
    one, return 0 instead.

    Example: `target = 7, [2, 3, 1, 2, 4, 3]` -> `2` (the subarray `[4, 3]` has the minimal length under the problem
    constraint)

    Sliding window: expand the right edge, then shrink from the left while the sum stays over target.
    """
    answer = None
    left = 0
    total = 0

    for index, _ in enumerate(numbers):
        total += numbers[index]
        while total >= target:
            if answer:
                answer = min(answer, index + 1 - left)
            else:
                answer = index + 1 - left
            total -= numbers[left]
            left += 1

    return answer if answer else 0
