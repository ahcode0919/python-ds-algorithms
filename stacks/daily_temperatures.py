"""Daily Temperatures.

Given a list of daily temperatures, return a list such that, for each day in the input, tells you how many days you
would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
The length of temperatures will be in the range [1, 30000]; each temperature will be an integer in the range
[30, 100].

Example: `T = [73, 74, 75, 71, 69, 72, 76, 73]` -> `[1, 1, 4, 2, 1, 1, 0, 0]`
"""

from collections import deque
from queue import LifoQueue


def daily_temperatures_brute_force(temps: list[int]) -> list[int]:
    """Brute-force: for each day, scan forward until a warmer temperature is found."""
    daily_temps = []
    for index, temp in enumerate(temps):
        count = 0
        for sub_index in range(index + 1, len(temps)):
            count += 1
            if temps[sub_index] > temp:
                break
            if sub_index == len(temps) - 1:
                count = 0
        daily_temps.append(count)
    return daily_temps


def daily_temperatures(temps: list[int]) -> list[int]:
    """Optimized: process right to left using a monotonic decreasing stack of indices."""
    daily_temps = deque()
    stack = LifoQueue()

    for index in range(len(temps) - 1, -1, -1):
        while not stack.empty() and temps[index] >= temps[stack.queue[-1]]:
            stack.get()

        if not stack.empty():
            daily_temps.appendleft(stack.queue[-1] - index)
        else:
            daily_temps.appendleft(0)
        stack.put(index)
    return list(daily_temps)
