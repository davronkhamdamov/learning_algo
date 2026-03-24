# Two Pointers (Category 2)

This folder contains your second category: **Two Pointers**.

For each problem, solutions are organized from **bad/brute force** to **best/optimal** and include detailed explanations + complexity.

- Implementations: `solutions.py`
- Explanations + classifications: this file

---

## Prerequisite

- **Two Pointers** (Advanced Algorithms)

---

## Classification Used

Each problem is classified by:
1. **Primary pattern**
2. **Difficulty**
3. **Optimal key idea**

---

## 1) Valid Palindrome

- **Pattern:** Two Pointers + Character Filtering
- **Difficulty:** Easy
- **Optimal key idea:** move left/right pointers inward while skipping non-alphanumeric chars.

### Approaches

1. **Bad (Build cleaned string + compare reverse manually)**
   - Build filtered lowercase string, then compare characters from both ends.
   - Time: `O(n)`, Space: `O(n)`.

2. **Best (In-place Two Pointers on original string)**
   - No cleaned copy needed. Skip invalid chars on the fly.
   - Time: `O(n)`, Space: `O(1)`.

---

## 2) Two Sum II - Input Array Is Sorted

- **Pattern:** Two Pointers on Sorted Array
- **Difficulty:** Medium
- **Optimal key idea:** if sum is too small move left, if too big move right.

### Approaches

1. **Bad (Brute Force Pair Search)**
   - Try all pairs.
   - Time: `O(n^2)`, Space: `O(1)`.

2. **Better (Binary Search for complement per index)**
   - For each index `i`, binary search `target - numbers[i]` in the suffix.
   - Time: `O(n log n)`, Space: `O(1)`.

3. **Best (Two Pointers)**
   - Start at both ends and shrink window based on sum.
   - Time: `O(n)`, Space: `O(1)`.

---

## 3) 3Sum

- **Pattern:** Sorting + Two Pointers
- **Difficulty:** Medium
- **Optimal key idea:** sort, fix one number, solve remaining two-sum via two pointers while skipping duplicates.

### Approaches

1. **Bad (Triple Nested Loops)**
   - Check every triplet.
   - Time: `O(n^3)`, Space: `O(1)`.

2. **Better (Fix one + hash set two-sum)**
   - For each `i`, use set for complements among remaining items.
   - Time: `O(n^2)`, Space: `O(n)`.

3. **Best (Sorted + Two Pointers with duplicate skipping)**
   - Sort once; for each fixed `i`, use `l`/`r` to find zero sum.
   - Time: `O(n^2)`, Space: `O(1)` extra excluding output.

---

## 4) Container With Most Water

- **Pattern:** Two Pointers + Greedy
- **Difficulty:** Medium
- **Optimal key idea:** area limited by shorter line; move shorter side inward.

### Approaches

1. **Bad (Check every pair)**
   - Compute all `O(n^2)` container areas.

2. **Best (Two Pointers Greedy)**
   - Start widest, repeatedly move shorter wall pointer.
   - Time: `O(n)`, Space: `O(1)`.

---

## 5) Trapping Rain Water

- **Pattern:** Two Pointers with running maxes
- **Difficulty:** Hard
- **Optimal key idea:** trapped water at side with smaller max is determined immediately.

### Approaches

1. **Bad (For each index, scan left max and right max)**
   - Time: `O(n^2)`, Space: `O(1)`.

2. **Better (Prefix max + suffix max arrays)**
   - Precompute left/right max arrays, then sum water.
   - Time: `O(n)`, Space: `O(n)`.

3. **Best (Two Pointers + left_max/right_max)**
   - Keep running maxima from both ends and accumulate as pointers move.
   - Time: `O(n)`, Space: `O(1)`.

---

## Notes

- Function naming in `solutions.py`:
  - `_bad` = brute-force or weak baseline
  - `_better` = meaningful improvement
  - `_best` = optimal/common interview solution
