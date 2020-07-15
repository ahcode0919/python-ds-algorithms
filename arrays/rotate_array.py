from typing import List


def rotate_array_with_array(nums: List[int], k: int) -> List[int]:
    copy = []
    count = 0
    index = k + 1
    length = len(nums)

    while count < length:
        copy.append(nums[index])
        index = (index + 1) % length
        count += 1

    return copy
