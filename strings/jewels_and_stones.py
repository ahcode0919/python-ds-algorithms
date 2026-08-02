"""Jewels and Stones.

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have. Determine how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Example: `J = "aA"`, `S = "aAAbbbb"` -> `3`
"""


def jewels_and_stones(jewels: str, stones: str) -> int:
    """Count occurrences of each stone, then sum the counts for stones that are also jewels."""
    stone_count = dict()

    for stone in stones:
        if stone in stone_count:
            stone_count[stone] += 1
        else:
            stone_count[stone] = 1

    count = 0
    jewel_set = set(jewels)

    for jewel in jewel_set:
        if jewel in stone_count:
            count += stone_count[jewel]

    return count
