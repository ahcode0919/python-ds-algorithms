# Linked Lists

* [Detect Cycle](#detect-cycle)
* [Intersection Two Linked Lists](#intersection-two-linked-lists)
* [Linked List Cycle](#linked-list-cycle)
* [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)

## Detect Cycle

Given a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

Solution with slow/fast

Time: O(N), Space: O(1)

```python
def detect_cycle(head: ListNode) -> Optional[ListNode]:
    # detect cycle
    if not head or not head.next:
        return None
    slow: ListNode = head
    fast: ListNode = head
    intersection: Optional[ListNode] = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersection = slow
            break

    if not intersection:
        return intersection

    # detect intersection
    node = head
    while node != intersection:
        node = node.next
        intersection = intersection.next

    return intersection
```

Solution with set

Time: O(N), Space: O(1)

```python
def detect_cycle_with_set(head: ListNode) -> Optional[ListNode]:
    visited_nodes: Set[ListNode] = set()

    node = head

    while node:
        if node and node in visited_nodes:
            return node
        visited_nodes.add(node)
        node = node.next
    return None
```

## Intersection Two Linked Lists

Find the node at which the intersection of two singly linked lists begins

Example:

a1 -> a2 -> a3 \
                -> c1 -> c2 -> c3
      b1 -> b2 /
      
Answer: c1

Solution using two pointers:

Time: O(N), Space: O(1)
      
```python
def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    if not head_a or not head_b:
        return None
    
    node_a: ListNode = head_a
    node_b: ListNode = head_b

    while node_a != node_b:
        node_a = node_a.next
        node_b = node_b.next

        if node_a is None and node_b is None:
            return None

        if node_a is None:
            node_a = head_b

        if node_b is None:
            node_b = head_a

    return node_a
```

Solution using Set (less optimal)

Time: O(N), Space: O(N)

```python
def get_intersection_node_with_set(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    nodes: Set[ListNode] = set()
    node_a: ListNode = head_a
    node_b: ListNode = head_b

    while node_a or node_b:
        if node_a:
            if node_a in nodes:
                return node_a
            nodes.add(node_a)
            node_a = node_a.next

        if node_b:
            if node_b in nodes:
                return node_b
            nodes.add(node_b)
            node_b = node_b.next

    return None
```

## Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

```python
# Time: O(N + K) -> O(N), Space: O(1)
def has_cycle(head: Optional['ListNode']) -> bool:
    if not head or not head.next:
        return False

    slow: ListNode = head
    fast: ListNode = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
```

Solution with set (less optimal)

```python
# Time: O(N), Space: O(N)
def has_cycle_with_set(head: Optional['ListNode']) -> bool:
    if not head or not head.next:
        return False

    node_set: Set[ListNode] = set()
    node: ListNode = head

    while node:
        if not node or node in node_set:
            return True
        node_set.add(node)
        node = node.next
    return False
```

## Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Time: O(N), Space: O(1)

```python
def remove_nth_from_end(head: ListNode, nth: int) -> Optional[ListNode]:
    dummy: ListNode = ListNode(0)
    dummy.next = head
    previous: ListNode = dummy
    lead: ListNode = dummy

    # Move lead forward
    for _ in range(nth + 1):
        lead = lead.next

    # Move through list until lead is None
    while lead:
        previous = previous.next
        lead = lead.next

    # Delete Node by relinking nodes or reassigning head
    previous.next = previous.next.next
    return dummy.next
```