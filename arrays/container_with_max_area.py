"""Container With Max Area.

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai), n vertical
lines are drawn such that the two endpoints of line i are at (i, ai) and (i, 0). Find two lines that, together
with the x-axis, form a container holding the most water.
"""

from typing import List


def container_with_max_area(height: List[int]) -> int:
    """Two-pointer sweep inward from both ends, tracking the largest area seen."""
    length = len(height)
    left = 0
    right = length - 1
    max_area = 0

    while left < right:
        lowest = min(height[left], height[right])
        max_area = max(max_area, lowest * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
