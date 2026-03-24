"""Linked List category solutions from bad -> best."""

from __future__ import annotations

import heapq
from typing import Dict, List, Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class RandomNode:
    def __init__(
        self,
        x: int,
        next: Optional["RandomNode"] = None,
        random: Optional["RandomNode"] = None,
    ):
        self.val = int(x)
        self.next = next
        self.random = random


# 1) REVERSE LINKED LIST

def reverse_list_bad(head: Optional[ListNode]) -> Optional[ListNode]:
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next

    dummy = ListNode()
    tail = dummy
    for v in reversed(vals):
        tail.next = ListNode(v)
        tail = tail.next

    return dummy.next


def reverse_list_best(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


# 2) MERGE TWO SORTED LISTS

def merge_two_lists_bad(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    vals = []

    cur = list1
    while cur:
        vals.append(cur.val)
        cur = cur.next

    cur = list2
    while cur:
        vals.append(cur.val)
        cur = cur.next

    vals.sort()
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next

    return dummy.next


def merge_two_lists_best(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    a, b = list1, list2
    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a else b
    return dummy.next


# 3) LINKED LIST CYCLE

def has_cycle_bad(head: Optional[ListNode]) -> bool:
    seen = set()
    cur = head
    while cur:
        if id(cur) in seen:
            return True
        seen.add(id(cur))
        cur = cur.next
    return False


def has_cycle_best(head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# 4) REORDER LIST

def reorder_list_bad(head: Optional[ListNode]) -> None:
    if not head:
        return

    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    left, right = 0, len(nodes) - 1
    while left < right:
        nodes[left].next = nodes[right]
        left += 1
        if left == right:
            break
        nodes[right].next = nodes[left]
        right -= 1

    nodes[left].next = None


def reorder_list_best(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev = None
    cur = second
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    second = prev

    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


# 5) REMOVE NTH NODE FROM END

def remove_nth_from_end_bad(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next

    idx_to_remove = length - n
    dummy = ListNode(0, head)
    cur = dummy
    for _ in range(idx_to_remove):
        cur = cur.next

    cur.next = cur.next.next
    return dummy.next


def remove_nth_from_end_best(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    first = second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


# 6) COPY LIST WITH RANDOM POINTER

def copy_random_list_bad(head: Optional[RandomNode]) -> Optional[RandomNode]:
    # Bad baseline: copies next chain but ignores random pointers completely.
    if not head:
        return None

    dummy = RandomNode(0)
    tail = dummy
    cur = head

    while cur:
        tail.next = RandomNode(cur.val)
        tail = tail.next
        cur = cur.next

    return dummy.next


def copy_random_list_best(head: Optional[RandomNode]) -> Optional[RandomNode]:
    if not head:
        return None

    old_to_new: Dict[RandomNode, RandomNode] = {}
    cur = head

    while cur:
        old_to_new[cur] = RandomNode(cur.val)
        cur = cur.next

    cur = head
    while cur:
        copy_node = old_to_new[cur]
        copy_node.next = old_to_new.get(cur.next)
        copy_node.random = old_to_new.get(cur.random)
        cur = cur.next

    return old_to_new[head]


# 7) ADD TWO NUMBERS

def add_two_numbers_bad(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def to_int(node: Optional[ListNode]) -> int:
        mul = 1
        total = 0
        cur = node
        while cur:
            total += cur.val * mul
            mul *= 10
            cur = cur.next
        return total

    total = to_int(l1) + to_int(l2)
    if total == 0:
        return ListNode(0)

    dummy = ListNode()
    tail = dummy
    while total > 0:
        tail.next = ListNode(total % 10)
        tail = tail.next
        total //= 10

    return dummy.next


def add_two_numbers_best(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    carry = 0

    a, b = l1, l2
    while a or b or carry:
        v1 = a.val if a else 0
        v2 = b.val if b else 0

        total = v1 + v2 + carry
        carry = total // 10

        tail.next = ListNode(total % 10)
        tail = tail.next

        if a:
            a = a.next
        if b:
            b = b.next

    return dummy.next


# 8) FIND THE DUPLICATE NUMBER

def find_duplicate_bad(nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


def find_duplicate_best(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow


# 9) LRU CACHE

class LRUCacheBad:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: List[Tuple[int, int]] = []  # [(key, value)], most recent at end

    def get(self, key: int) -> int:
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items.pop(i)
                self.items.append((k, v))
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        for i, (k, _) in enumerate(self.items):
            if k == key:
                self.items.pop(i)
                self.items.append((key, value))
                return

        if len(self.items) == self.capacity:
            self.items.pop(0)
        self.items.append((key, value))


class _DNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev: Optional[_DNode] = None
        self.next: Optional[_DNode] = None


class LRUCacheBest:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: Dict[int, _DNode] = {}

        self.left = _DNode()  # LRU sentinel
        self.right = _DNode()  # MRU sentinel
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: _DNode) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_mru(self, node: _DNode) -> None:
        prev_mru = self.right.prev
        prev_mru.next = node
        node.prev = prev_mru
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._remove(node)
        self._insert_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._insert_mru(node)
            return

        node = _DNode(key, value)
        self.map[key] = node
        self._insert_mru(node)

        if len(self.map) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.map[lru.key]


# 10) MERGE K SORTED LISTS

def merge_k_lists_bad(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    vals = []
    for head in lists:
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

    if not vals:
        return None

    vals.sort()
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next

    return dummy.next


def merge_k_lists_best(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    counter = 0

    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, counter, node))
            counter += 1

    dummy = ListNode()
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    tail.next = None
    return dummy.next


# 11) REVERSE NODES IN K GROUP

def reverse_k_group_bad(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next

    for i in range(0, len(vals), k):
        if i + k <= len(vals):
            vals[i : i + k] = reversed(vals[i : i + k])

    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next

    return dummy.next


def reverse_k_group_best(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def get_kth(curr: Optional[ListNode], steps: int) -> Optional[ListNode]:
        while curr and steps > 0:
            curr = curr.next
            steps -= 1
        return curr

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev, cur = group_next, group_prev.next
        while cur != group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return dummy.next
