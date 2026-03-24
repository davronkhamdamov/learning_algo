# Sliding Window (Category 5)

This folder contains your fifth category: **Sliding Window**.

For each problem, solutions are presented from **bad/brute-force** to **best/optimal** with clear pattern classification and complexity.

- Implementations: `solutions.py`
- Explanations + classifications: this file

---

## Prerequisites

- **Sliding Window Fixed Size** (Advanced Algorithms)
- **Sliding Window Variable Size** (Advanced Algorithms)

---

## Classification Used

Each problem includes:
1. **Primary pattern**
2. **Difficulty**
3. **Optimal key idea**

---

## 1) Best Time to Buy And Sell Stock

- **Pattern:** Running minimum (variable-size window intuition)
- **Difficulty:** Easy
- **Optimal key idea:** track the minimum price seen so far and max profit at each day.

### Approaches

1. **Bad (Check all buy/sell pairs)**
   - Time: `O(n^2)`, Space: `O(1)`.

2. **Best (One pass running min)**
   - Time: `O(n)`, Space: `O(1)`.

---

## 2) Longest Substring Without Repeating Characters

- **Pattern:** Variable-size sliding window + hash set/map
- **Difficulty:** Medium
- **Optimal key idea:** expand right pointer and shrink left pointer until window has unique chars.

### Approaches

1. **Bad (Start from each index and extend until duplicate)**
   - Time: `O(n^2)`, Space: `O(k)`.

2. **Best (Sliding window with last seen indices / set shrink)**
   - Time: `O(n)`, Space: `O(k)`.

---

## 3) Longest Repeating Character Replacement

- **Pattern:** Variable-size sliding window + frequency counts
- **Difficulty:** Medium
- **Optimal key idea:** valid window if `(window_size - max_char_freq) <= k`.

### Approaches

1. **Bad (Try all substrings and test if fixable with <=k edits)**
   - Time: `O(n^3)` (or `O(n^2 * alphabet)` with optimization).

2. **Best (Sliding window with running max frequency)**
   - Time: `O(n)`, Space: `O(1)` for uppercase alphabet.

---

## 4) Permutation in String

- **Pattern:** Fixed-size sliding window + frequency comparison
- **Difficulty:** Medium
- **Optimal key idea:** maintain a window of length `len(s1)` and compare counts efficiently.

### Approaches

1. **Bad (Sort each window of s2 and compare to sorted s1)**
   - Time: `O((n-m+1) * m log m)`.

2. **Better (Frequency arrays, compare arrays each shift)**
   - Time: `O((n-m+1) * alphabet)`.

3. **Best (Frequency arrays + matched-count tracking)**
   - Time: `O(n)`, Space: `O(1)`.

---

## 5) Minimum Window Substring

- **Pattern:** Variable-size sliding window + need/have counting
- **Difficulty:** Hard
- **Optimal key idea:** expand to satisfy all required chars, then shrink to get minimal valid window.

### Approaches

1. **Bad (Check all substrings for coverage)**
   - Time: `O(n^3)` style brute force.

2. **Best (Two pointers + frequency maps)**
   - Time: `O(n)` average with hash maps, Space: `O(k)`.

---

## 6) Sliding Window Maximum

- **Pattern:** Fixed-size sliding window + monotonic deque
- **Difficulty:** Hard
- **Optimal key idea:** maintain deque of indices in decreasing value order.

### Approaches

1. **Bad (Recompute max for each window)**
   - Time: `O((n-k+1)*k)`.

2. **Best (Monotonic deque)**
   - Time: `O(n)`, Space: `O(k)`.

---

## Notes

- Naming in `solutions.py`:
  - `_bad` = brute force / baseline
  - `_better` = improved midpoint approach
  - `_best` = canonical optimal interview approach
