# N-ary Tree

Similar to a binary tree except Nodes can have any number of child Nodes.

```
        A
     /  |  \
    B   C   D
   / \    / | \
  E   F  H  I  J
 /     \
K       L
```

* [Level Order Traversal](#level-order-traversal)
* [Max Depth](#max-depth)
* [Postorder Traversal](#postorder-traversal)
* [Preorder Traversal](#preorder-traversal)

## Level Order Traversal

Return N-nary tree level by level as a nested array.

Example: `[[A], [B, C, D], [E, F, H, I, J], [K, L]]`

```python
def level_order_traversal(root: Node) -> List[List[int]]:
    levels = []

    if not root:
        return levels

    current_level = [root]

    while current_level:
        next_level = []
        values = []

        for node in current_level:
            if node.children:
                next_level.extend(node.children)
            values.append(node.value)

        levels.append(values)
        current_level = next_level

    return levels
```

## Max Depth

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```python
def max_depth_top_down(root: Node) -> int:
    def traverse(node, depth):
        if not node:
            return depth

        maximum_depth = depth

        if node.children:
            for child in node.children:
                maximum_depth = max(maximum_depth, traverse(child, depth + 1))
        return maximum_depth

    if not root:
        return 0

    return traverse(root, 1)


def max_depth_bottom_up(root: Node) -> int:
    if not root:
        return 0

    depth = 1

    if root.children:
        for child in root.children:
            depth = max(depth, max_depth_bottom_up(child) + 1)

    return depth
```

## Postorder Traversal

Recursive

```python
def postorder_traversal(root: Optional[Node]) -> List:
    values = []

    if not root:
        return values

    if root.children:
        for child in root.children:
            values.extend(postorder_traversal(child))
    values.append(root.value)

    return values
```

Iterative:

```python
def postorder_traversal_iterative(root: Optional[Node]) -> List:
    values = deque()
    stack = []
    if not root:
        return []

    stack.append(root)

    while stack:
        node = stack.pop()
        if node.children:
            for child in node.children:
                stack.append(child)
        values.appendleft(node.value)

    return list(values)
```

## Preorder Traversal

Recursive

```python
def preorder_traversal(root: Node) -> List:
    if not root:
        return []

    values = [root.value]

    for child in root.children:
        values.extend(preorder_traversal(child))

    return values
```

Iterative

```python
def preorder_traversal_iterative(root: Node) -> List:
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.value)

        if node.children:
            for child in reversed(node.children):
                stack.append(child)

    return values
```