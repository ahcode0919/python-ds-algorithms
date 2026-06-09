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
* [Pre-order Traversal](#pre-order-traversal)

## Pre-order Traversal

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