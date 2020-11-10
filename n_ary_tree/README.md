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

* [Postorder Traversal](#postorder-traversal)
* [Preorder Traversal](#preorder-traversal)

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