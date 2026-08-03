def remove_duplicates(nums: list[int]) -> int:
    """Remove Duplicates.

    Given a sorted array nums, remove the duplicates in-place such that each element appears only once, and return
    the new length. Do not allocate extra space for another array; modify the input array in-place with O(1) extra
    memory.

    Example: `[1, 1, 2]` -> `[1, 2, 2], count: 2`

    Two-pointer in-place compaction over an already-sorted array.
    """
    if len(nums) <= 1:
        return len(nums)

    last_index = 0

    for index in range(1, len(nums)):
        if nums[index] == nums[last_index]:
            continue
        last_index += 1
        nums[last_index] = nums[index]

    return last_index + 1
