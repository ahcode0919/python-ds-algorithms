# Queues

* [Implement Queue With Stack](#implement-queue-with-stack)
* [Moving Average](#moving-average)
* [Walls and Gates (BFS)](#walls-and-gates-bfs)

## Implement Queue With Stack

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.


Example:

```python
queue = MyQueue()

queue.push(1)
queue.push(2)  
queue.peek()  # returns 1
queue.pop()   # returns 1
queue.empty() # returns false
```

```python
class Queue(Generic[T]):
    def __init__(self):
        self.queue: Deque[T] = deque()

    def push(self, item: T) -> None:
        self.queue.append(item)

    def pop(self) -> T:
        return self.queue.popleft()

    def peek(self) -> T:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
```


## Moving Average

Leetcode: Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

```python
m = MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```

```python
class MovingAverage:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.queue = deque()

    def next(self, number: int) -> float:
        self.queue.append(number)

        if len(self.queue) > self.max_size:
            self.queue.popleft()

        return sum(self.queue) / float(len(self.queue))
```

## Walls and Gates (BFS)

You are given a m x n 2D grid initialized with these three possible values.

`-1`  - A wall or an obstacle.
`0`   - A gate.
`INF` - Infinity means an empty room. We use the value `2^31 - 1 = 2147483647` to represent INF as you may assume that the distance to a gate is less than `2147483647`.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

```
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
```

After running your function, the 2D grid should be:
```
3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4
```

```python
def walls_and_gates(rooms: List[List[int]]) -> None:
    height = len(rooms)
    if height == 0:
        return

    width = len(rooms[0])
    queue = deque()

    for row in range(height):
        for col in range(width):
            if rooms[row][col] == 0:
                queue.appendleft((row, col))

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        point = queue.pop()
        for direction in directions:
            row = point[0] + direction[0]
            col = point[1] + direction[1]
            if row < 0 or col < 0 or row >= height or col >= width or rooms[row][col] != 2147483647:
                continue
            rooms[row][col] = rooms[point[0]][point[1]] + 1
            queue.appendleft((row, col))
```