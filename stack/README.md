# Stack (Category 3)

This folder contains your third category: **Stack**.

For every problem, solutions are organized from **bad/brute-force** to **best/optimal** and include classification + complexity analysis.

- Implementations: `solutions.py`
- Explanations + classifications: this file

---

## Prerequisite

- **Stacks** (Data Structures & Algorithms for Beginners)

---

## Classification Used

Each problem includes:
1. **Primary pattern**
2. **Difficulty**
3. **Optimal key idea**

---

## 1) Valid Parentheses

- **Pattern:** Stack (LIFO)
- **Difficulty:** Easy
- **Optimal key idea:** push opening brackets and match closing brackets against stack top.

### Approaches

1. **Bad (Repeated String Replacement)**
   - Repeatedly remove `()`, `{}`, `[]` until no change.
   - Simple conceptually but inefficient due to repeated scans/reallocations.
   - Time: up to `O(n^2)`, Space: `O(n)`.

2. **Best (Single-Pass Stack)**
   - On open bracket push expected close (or push open and map).
   - On close bracket ensure it matches top.
   - Time: `O(n)`, Space: `O(n)`.

---

## 2) Min Stack

- **Pattern:** Stack + Auxiliary Min Tracking
- **Difficulty:** Medium
- **Optimal key idea:** keep a parallel stack of minimums so `getMin()` is `O(1)`.

### Approaches

1. **Bad (Single list + scan min on demand)**
   - `getMin()` scans all values each call.
   - `push/pop/top` are `O(1)`; `getMin` is `O(n)`.

2. **Best (Two Stacks)**
   - `vals` stores values, `mins` stores min-so-far at each depth.
   - All methods `O(1)` time.

---

## 3) Evaluate Reverse Polish Notation

- **Pattern:** Stack-based expression evaluation
- **Difficulty:** Medium
- **Optimal key idea:** push numbers; on operator pop two values, evaluate, push result.

### Approaches

1. **Bad (Re-scan tokens and collapse one operator at a time)**
   - Simulates evaluation with repeated list edits.
   - Time can degrade near `O(n^2)`.

2. **Best (Single Stack Pass)**
   - Process tokens once; apply operation immediately.
   - Time: `O(n)`, Space: `O(n)`.

---

## 4) Daily Temperatures

- **Pattern:** Monotonic Decreasing Stack of indices
- **Difficulty:** Medium
- **Optimal key idea:** when current temp is higher, resolve prior colder days from stack.

### Approaches

1. **Bad (Nested loops for next warmer day)**
   - For each day, scan forward until warmer day found.
   - Time: `O(n^2)`, Space: `O(1)`.

2. **Best (Monotonic Stack)**
   - Stack keeps indices with unresolved warmer day, descending temperatures.
   - Time: `O(n)`, Space: `O(n)`.

---

## 5) Car Fleet

- **Pattern:** Sorting + Stack-like merge logic
- **Difficulty:** Medium
- **Optimal key idea:** process cars from closest-to-target backward; slower arrival time ahead absorbs faster behind.

### Approaches

1. **Bad (Discrete simulation by time steps)**
   - Move cars in small increments and check merges.
   - Very slow and numerically awkward.

2. **Best (Sort by position descending + stack of arrival times)**
   - Compute each car’s arrival time.
   - If current time <= fleet ahead time, it merges; else new fleet.
   - Time: `O(n log n)` due to sorting, Space: `O(n)`.

---

## 6) Largest Rectangle in Histogram

- **Pattern:** Monotonic Increasing Stack
- **Difficulty:** Hard
- **Optimal key idea:** when height drops, pop taller bars and compute max area where popped height is limiting bar.

### Approaches

1. **Bad (All ranges min-height computation)**
   - Try every subarray and track minimum height.
   - Time: `O(n^2)` (or worse if min recomputed naively).

2. **Best (Monotonic Stack with start indices)**
   - Maintain increasing heights.
   - On drop, pop and compute rectangle widths immediately.
   - Time: `O(n)`, Space: `O(n)`.

---

## Notes

- Naming in `solutions.py`:
  - `_bad` = baseline brute-force/inefficient
  - `_best` = optimal common interview solution
- For OOP problem `Min Stack`, both a bad and best class are included.
