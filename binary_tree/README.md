# Binary Tree

* [Binary Tree Path](#binary-tree-path)
* [Has Path Sum](#has-path-sum)
* [In-order Traversal](#in-order-traversal)
* [Level-order Traversal](#level-order-traversal)
* [Max Depth](#max-depth)
* [Next Right Pointer](#next-right-pointer)
* [Post-order Traversal](#post-order-traversal)
* [Pre-order Traversal](#pre-order-traversal)
* [Symmetric Binary Tree](#symmetric-binary-tree)
* [Tree from Inorder and Postorder Traversal](#tree-from-inorder-and-postorder-traversal)
* [Valid Binary Search Tree](#valid-binary-search-tree)

## Binary Tree Path

Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:

Input:

```text
   1
 /   \
2     3
 \
  5
```
Output: `["1->2->5", "1->3"]`

Explanation: All root-to-leaf paths are: `1->2->5`, `1->3`

```python
def binary_tree_paths(root_node: TreeNode) -> str:
    paths = []
    if not root_node:
        return paths
    get_path(root_node, '', paths)
    return paths

def get_path(node: TreeNode, path: str, paths: []) -> str:
    if not node.left and not node.right:
        paths.append(path + str(node.val))
        return
    if node.left:
        get_path(node.left, path + str(node.val) + '->', paths)
    if node.right:
        get_path(node.right, path + str(node.val) + '->', paths)
```

## Has Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

```python
def has_path_sum(root: TreeNode, target: int) -> bool:
    if not root:
        return False

    target -= root.val

    if root.left or root.right:
        left = has_path_sum(root.left, target)
        right = has_path_sum(root.right, target)
        return left or right
    return target == 0
```

## In-order Traversal

In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.

Example:

```text
     1
    / \
   2   3
  / \
 4   5 
```
 
Output: `[4, 2, 5, 1, 1]`

In-order traversal recursively

```python
def inorder_traversal(root: TreeNode) -> List[int]:
    values = []

    if not root:
        return values

    if root.left:
        values.extend(inorder_traversal(root.left))
    values.append(root.val)

    if root.right:
        values.extend(inorder_traversal(root.right))

    return values
```

In-order traversal with stack

```python
def inorder_traversal_stack(root: TreeNode) -> List[int]:
    output = []
    stack = []
    current_node = root

    while current_node or len(stack) > 0:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        output.append(current_node.val)
        current_node = current_node.right

    return output
```

## Level-order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example:

```text
    1
   / \
  2   3
    /   \
   4     5
```

`[
  [1],
  [2, 3],
  [4, 5]
]`

```python
def level_order_traversal(root: TreeNode) -> List[List[int]]:
    values = []

    if not root:
        return values

    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        values.append(level)

    return values
```

## Max Depth

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```python
def max_depth(root: TreeNode) -> int:
    max_level = 0

    if not root:
        return max_level

    level = [root]

    while level:
        max_level += 1
        next_level = []

        while len(level) > 0:
            node = level.pop()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level

    return max_level
```

## Next Right Pointer

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to `None`

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


def next_right_pointer(root: Node) -> Node:
    if not root:
        return root

    level = deque([root])

    while level:
        right = None

        for _ in range(len(level)):
            left = level.pop()
            left.next = right
            right = left
            if left.right:
                level.appendleft(left.right)
            if left.left:
                level.appendleft(left.left)

    return root
```

## Post-order Traversal

Algorithm Postorder(tree)
   1. Traverse the left subtree
   2. Traverse the right subtree
   3. Visit the root.

Example:
```text
     1
    / \
   2   3
  / \
 4   5 
 ```
Output: `[4, 5, 2, 3, 1]`
   
Recursive Approach:

 ```python
def postorder_traversal_recursive(root: TreeNode) -> List[int]:
    values = []
    if not root:
        return values

    if root.left:
        values.extend(postorder_traversal_recursive(root.left))
    if root.right:
        values.extend(postorder_traversal_recursive(root.right))

    values.append(root.val)

    return values
```

Iterative Approach:

```python
def postorder_traversal_iterative(root: TreeNode) -> List[int]:
    values = []
    stack = []

    while root or stack:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()

        if stack and root.right == stack[-1]:
            stack[-1] = root
            root = root.right
        else:
            values.append(root.val)
            root = None

    return values
```

## Pre-order Traversal

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

Example:

```text
     1
    / \
   2   3
  / \
 4   5 
 ```

Output: `[1, 2, 4, 5, 3]`

Iterative approach Time: O(N), Space: O(N)

```python
def preorder_traversal_iterative(root: TreeNode) -> List[int]:
    output = []

    if root is None:
        return output

    stack = [root]
    while stack:
        root_node = stack.pop()
        if root_node is not None:
            output.append(root_node.val)
        if root_node.right is not None:
            stack.append(root_node.right)
        if root_node.left is not None:
            stack.append(root_node.left)
    return output
```

Morris version. Time: O(N), Space: O(1)

```python
def preorder_traversal_morris(root: TreeNode) -> List[int]:
    node, output = root, []
    while node:
        if not node.left:
            output.append(node.val)
            node = node.right
        else:
            predecessor = node.left

            while predecessor.right and predecessor.right is not node:
                predecessor = predecessor.right

            if not predecessor.right:
                output.append(node.val)
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                node = node.right

    return output
```

Time: O(N), Space: O(N)

```python
def preorder_traversal_recursive(root: TreeNode) -> List[int]:
    values = []
    if not root:
        return values

    values.append(root.val)

    if root.left:
        values.extend(preorder_traversal_recursive(root.left))
    if root.right:
        values.extend(preorder_traversal_recursive(root.right))
    return values
```

## Symmetric Binary Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1, 2, 2, 3, 4, 4, 3]` is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following `[1 ,2, 2, null, 3, null, 3]` is not:

```
    1
   / \
  2   2
   \   \
   3    3
```

```python
def symmetric_binary_tree(root: Optional[TreeNode]) -> bool:
    level = [root]

    while level:
        next_level = []
        left = 0
        right = len(level) - 1

        while left <= right:
            left_val = level[left].val if level[left] else None
            right_val = level[right].val if level[right] else None

            if left_val != right_val:
                return False

            left += 1
            right -= 1

        for node in level:
            if node:
                next_level.append(node.left)
                next_level.append(node.right)

        level = next_level

    return True
```

## Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.

For example, given

inorder = `[9, 3, 15, 20, 7]` - Left -> Node -> Right
postorder = `[9, 15, 7, 20, 3]` - Left -> Right -> Node

Return the following binary tree:

```text
    3
   / \
  9  20
    /  \
   15   7
```

```python
def tree_from_inorder_and_postorder(inorder: List[int], postorder: List[int]) -> TreeNode:
    def helper(in_left, in_right):
        if in_left > in_right:
            return None

        # last element is root
        value = postorder.pop()
        root = TreeNode(value)

        middle = index_map[value]

        root.right = helper(middle + 1, in_right)
        root.left = helper(in_left, middle - 1)

        return root

    index_map = {value: index for index, value in enumerate(inorder)}

    return helper(0, len(inorder) - 1)
```

## Valid Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

```python
def valid_bst(root: TreeNode, min_value=float('-inf'), max_value=float('inf')) -> bool:
    if not root:
        return True

    if not valid_bst(root.left, min_value, root.val):
        return False

    if not valid_bst(root.right, root.val, max_value):
        return False

    return min_value < root.val < max_value
```