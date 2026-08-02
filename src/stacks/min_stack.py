class MinStack:
    """Min Stack.

    Design a stack that supports push, pop, top, and retrieving the minimum element, all in constant time.

    Tracks the running minimum alongside each pushed value for O(1) getMin.
    """

    def __init__(self):
        # Tuple (value, current_min)
        self.stack = []

    def push(self, value: int) -> None:
        """Push value onto the stack, storing the minimum seen so far alongside it."""
        if len(self.stack) == 0:
            self.stack.append((value, value))
        else:
            self.stack.append((value, min(value, self.stack[-1][1])))

    def pop(self) -> None:
        """Remove the top (value, min) pair from the stack."""
        self.stack.pop()

    def top(self) -> int:
        """Return the value on top of the stack."""
        return self.stack[-1][0]

    def get_min(self) -> int:
        """Return the minimum value currently in the stack."""
        return self.stack[-1][1]
