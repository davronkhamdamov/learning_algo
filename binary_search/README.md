# Binary Search (Category 4)

This folder contains your fourth category: **Binary Search**.

Each problem is explained from **bad/brute-force** to **best/optimal** with classification and complexity notes.

- Implementations: `solutions.py`
- Explanations + classifications: this file

---

## Prerequisites

- **Search Array** (Data Structures & Algorithms for Beginners)
- **Search Range** (Data Structures & Algorithms for Beginners)

---

## Classification Used

Each problem includes:
1. **Primary pattern**
2. **Difficulty**
3. **Optimal key idea**

---

## 1) Binary Search

- **Pattern:** Classic Binary Search on sorted array
- **Difficulty:** Easy
- **Optimal key idea:** repeatedly halve the search interval by comparing midpoint with target.

### Approaches

1. **Bad (Linear scan)**
   - Check each element in order.
   - Time: `O(n)`, Space: `O(1)`.

2. **Best (Binary search)**
   - Time: `O(log n)`, Space: `O(1)`.

---

## 2) Search a 2D Matrix

- **Pattern:** Binary Search on flattened sorted matrix
- **Difficulty:** Medium
- **Optimal key idea:** treat matrix as a virtual sorted 1D array.

### Approaches

1. **Bad (Full matrix scan)**
   - Time: `O(m*n)`, Space: `O(1)`.

2. **Better (Find row then binary search in row)**
   - First locate candidate row, then binary search inside.
   - Time: `O(m + log n)` (or `O(log m + log n)` if both steps are binary).

3. **Best (Single binary search over [0..m*n-1])**
   - Convert index `mid` into row/col via division/modulo.
   - Time: `O(log(m*n))`, Space: `O(1)`.

---

## 3) Koko Eating Bananas

- **Pattern:** Binary Search on Answer Space
- **Difficulty:** Medium
- **Optimal key idea:** predicate `can_finish(speed)` is monotonic.

### Approaches

1. **Bad (Try every speed from 1 to max pile)**
   - Time: `O(max_pile * n)`.

2. **Best (Binary search minimum feasible speed)**
   - Search `k` in `[1, max(piles)]`.
   - Time: `O(n log max_pile)`, Space: `O(1)`.

---

## 4) Find Minimum in Rotated Sorted Array

- **Pattern:** Binary Search with rotation property
- **Difficulty:** Medium
- **Optimal key idea:** compare middle with right boundary to decide which half contains minimum.

### Approaches

1. **Bad (Linear minimum search)**
   - Time: `O(n)`, Space: `O(1)`.

2. **Best (Binary search on rotated break)**
   - Time: `O(log n)`, Space: `O(1)`.

---

## 5) Search in Rotated Sorted Array

- **Pattern:** Binary Search with sorted-half detection
- **Difficulty:** Medium
- **Optimal key idea:** at least one half is sorted; decide target side accordingly.

### Approaches

1. **Bad (Linear search)**
   - Time: `O(n)`, Space: `O(1)`.

2. **Best (Modified binary search)**
   - Time: `O(log n)`, Space: `O(1)`.

---

## 6) Time Based Key Value Store

- **Pattern:** Hash Map + Binary Search on timestamps
- **Difficulty:** Medium
- **Optimal key idea:** for each key, timestamps are stored in sorted insertion order; use binary search for latest <= query time.

### Approaches

1. **Bad (Per-key list scan backward/forward at query time)**
   - `set`: `O(1)` append
   - `get`: up to `O(k)` where `k` is writes for key.

2. **Best (Per-key list + binary search get)**
   - `set`: `O(1)` append
   - `get`: `O(log k)`.

---

## 7) Median of Two Sorted Arrays

- **Pattern:** Binary Search Partitioning
- **Difficulty:** Hard
- **Optimal key idea:** partition two arrays so left side size equals right side size and left max <= right min.

### Approaches

1. **Bad (Merge fully then read median)**
   - Time: `O(m+n)`, Space: `O(m+n)`.

2. **Better (Two-pointer partial merge until median point)**
   - Time: `O(m+n)`, Space: `O(1)` extra.

3. **Best (Binary search on smaller array partition)**
   - Time: `O(log(min(m,n)))`, Space: `O(1)`.

---

## Notes

- Naming in `solutions.py`:
  - `_bad` = brute-force/baseline
  - `_better` = improved but not optimal
  - `_best` = canonical optimal interview solution
