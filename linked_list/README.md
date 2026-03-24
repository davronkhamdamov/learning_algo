# Linked List (Category 6)

This folder contains your sixth category: **Linked List**.

Problems are explained from **bad/brute-force** to **best/optimal** with classification and complexity.

- Implementations: `solutions.py`
- Explanations + classifications: this file

---

## Prerequisites

- **Singly Linked Lists** (Data Structures & Algorithms for Beginners)
- **Doubly Linked Lists** (Data Structures & Algorithms for Beginners)
- **Fast and Slow Pointers** (Advanced Algorithms)

---

## Classification Used

Each problem includes:
1. **Primary pattern**
2. **Difficulty**
3. **Optimal key idea**

---

## 1) Reverse Linked List
- **Pattern:** Pointer reversal
- **Difficulty:** Easy
- **Optimal key idea:** rewire `next` pointers iteratively in one pass.

Approaches:
1. **Bad:** copy values to array and rebuild list (`O(n)` extra space).
2. **Best:** in-place iterative reversal (`O(1)` extra space).

---

## 2) Merge Two Sorted Lists
- **Pattern:** Two-pointer merge on linked lists
- **Difficulty:** Easy
- **Optimal key idea:** attach smaller current node each step.

Approaches:
1. **Bad:** collect all values, sort, rebuild list.
2. **Best:** iterative pointer merge using dummy head.

---

## 3) Linked List Cycle
- **Pattern:** Fast/slow pointers
- **Difficulty:** Easy
- **Optimal key idea:** if cycle exists, fast and slow pointers meet.

Approaches:
1. **Bad:** track visited node ids in hash set.
2. **Best:** Floyd cycle detection with `O(1)` space.

---

## 4) Reorder List
- **Pattern:** Split + reverse + merge
- **Difficulty:** Medium
- **Optimal key idea:** find middle, reverse second half, interleave halves.

Approaches:
1. **Bad:** copy nodes into array and relink from both ends.
2. **Best:** in-place split/reverse/merge.

---

## 5) Remove Nth Node From End of List
- **Pattern:** Two pointers with fixed gap
- **Difficulty:** Medium
- **Optimal key idea:** advance first pointer `n` steps, then move both until first hits end.

Approaches:
1. **Bad:** compute length first, then remove `(len-n)`th node.
2. **Best:** one-pass two-pointer method with dummy node.

---

## 6) Copy List With Random Pointer
- **Pattern:** Hash map of old->new node (or weaving trick)
- **Difficulty:** Medium
- **Optimal key idea:** clone nodes and map original nodes to copied nodes.

Approaches:
1. **Bad:** recursive clone without memo (fails on shared/random references).
2. **Best:** two-pass hashmap clone.

---

## 7) Add Two Numbers
- **Pattern:** Linked list digit-by-digit addition with carry
- **Difficulty:** Medium
- **Optimal key idea:** simulate elementary addition while traversing both lists.

Approaches:
1. **Bad:** convert to integers and back (overflow/large integer concerns conceptually).
2. **Best:** carry-based linked-list addition.

---

## 8) Find The Duplicate Number
- **Pattern:** Fast/slow pointers in implicit linked list
- **Difficulty:** Medium
- **Optimal key idea:** treat value as next pointer index and apply Floyd cycle entrance logic.

Approaches:
1. **Bad:** hash set seen-check.
2. **Best:** Floyd cycle detection with `O(1)` extra space.

---

## 9) LRU Cache
- **Pattern:** Hash map + doubly linked list
- **Difficulty:** Medium
- **Optimal key idea:** hashmap for O(1) lookup, doubly linked list for O(1) move/remove.

Approaches:
1. **Bad:** list + dict with costly middle operations.
2. **Best:** custom doubly linked list + hash map, all ops `O(1)`.

---

## 10) Merge K Sorted Lists
- **Pattern:** Heap (priority queue) + linked lists
- **Difficulty:** Hard
- **Optimal key idea:** always extract smallest current head among k lists.

Approaches:
1. **Bad:** flatten values, sort, rebuild.
2. **Best:** min-heap over current heads.

---

## 11) Reverse Nodes in K Group
- **Pattern:** Segment reversal in linked list
- **Difficulty:** Hard
- **Optimal key idea:** reverse each full block of size `k`; leave remainder untouched.

Approaches:
1. **Bad:** array conversion and chunk reversal.
2. **Best:** in-place group reversal using pointer rewiring.

---

## Notes
- Naming in `solutions.py`:
  - `_bad` = baseline/brute-force
  - `_best` = canonical optimal approach
- Some problems include helper classes (`ListNode`, `RandomNode`, cache nodes).
