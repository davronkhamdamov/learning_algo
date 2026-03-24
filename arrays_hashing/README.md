# Arrays & Hashing (Category 1)

This folder contains the first category of problems you listed: **Arrays & Hashing**.

For each problem, solutions are organized from **bad/brute force** to **best/optimal**.

- Implementations: `solutions.py`
- Explanations + classifications: this file

---

## Classification Used

Each problem is classified by:

1. **Primary pattern** (Array, Hash Map, Hash Set, Sorting, Bucket/Heap, Prefix Product, etc.)
2. **Difficulty** (Easy/Medium)
3. **Key idea for optimal solution**

---

## Problems

## 1) Contains Duplicate

- **Pattern:** Array + Hash Set
- **Difficulty:** Easy
- **Optimal key idea:** track seen values in a set; duplicate appears if value already exists.

### Approaches

1. **Bad (Brute Force Double Loop)**
   - Compare every pair `(i, j)` where `i < j`.
   - If any equal pair is found, return `True`.
   - Time: `O(n^2)`, Space: `O(1)`.

2. **Better (Sort + Adjacent Check)**
   - Sort array and check neighboring values.
   - If `nums[i] == nums[i-1]`, duplicate exists.
   - Time: `O(n log n)`, Space: `O(1)` extra (or `O(n)` depending on sort implementation).

3. **Best (Hash Set)**
   - Iterate once; if value is in `seen`, return `True`, else add it.
   - Time: `O(n)` average, Space: `O(n)`.

---

## 2) Valid Anagram

- **Pattern:** Hash Frequency Counting
- **Difficulty:** Easy
- **Optimal key idea:** two strings are anagrams iff character frequencies match exactly.

### Approaches

1. **Bad (Permutation Generation)**
   - Generate all permutations of one string and compare to the other.
   - Time: `O(n!)`, Space: huge.

2. **Better (Sort Both Strings)**
   - Sort both and compare equality.
   - Time: `O(n log n)`, Space: `O(n)`.

3. **Best (Frequency Map / Counter)**
   - Count chars of `s`, decrement with `t`, ensure all zero.
   - Time: `O(n)`, Space: `O(1)` for fixed alphabet, else `O(k)`.

---

## 3) Two Sum

- **Pattern:** Array + Hash Map
- **Difficulty:** Easy
- **Optimal key idea:** store value -> index and look for complement `target - x` in one pass.

### Approaches

1. **Bad (Brute Force Double Loop)**
   - Check every pair.
   - Time: `O(n^2)`, Space: `O(1)`.

2. **Better (Sort + Two Pointers + Original Index Recovery)**
   - Sort value-index pairs; use two pointers.
   - Time: `O(n log n)`, Space: `O(n)`.

3. **Best (One-Pass Hash Map)**
   - For each value, check if complement already seen.
   - Time: `O(n)` average, Space: `O(n)`.

---

## 4) Group Anagrams

- **Pattern:** Hash Map + Canonical Signature
- **Difficulty:** Medium
- **Optimal key idea:** use a canonical key (char count tuple) for each string.

### Approaches

1. **Bad (Compare each word against existing groups by sorted equality)**
   - Potentially compare with many words/groups repeatedly.
   - Worst case can approach `O(n^2 * k log k)`.

2. **Better (Sorted String Key)**
   - Key = `"".join(sorted(word))`.
   - Time: `O(n * k log k)`, Space: `O(nk)`.

3. **Best (26-Length Frequency Tuple Key)**
   - Build char frequency tuple for each word.
   - Time: `O(n * k)`, Space: `O(nk)`.

---

## 5) Top K Frequent Elements

- **Pattern:** Hash Map + Bucketing/Heap
- **Difficulty:** Medium
- **Optimal key idea:** count frequencies, then use bucket sort by frequency.

### Approaches

1. **Bad (Count manually + repeatedly find max)**
   - Repeated scans over map for `k` selections.
   - Time roughly `O(n + k*m)` where `m` is unique count (can be near `O(n^2)`).

2. **Better (Sort by Frequency)**
   - Sort frequency map items descending.
   - Time: `O(n + m log m)`, Space: `O(m)`.

3. **Best (Bucket Sort by Frequency)**
   - Frequency range is `1..n`, place nums into buckets by count.
   - Scan buckets from high to low to collect `k`.
   - Time: `O(n)`, Space: `O(n)`.

---

## 6) Encode and Decode Strings

- **Pattern:** String Encoding + Parsing
- **Difficulty:** Medium
- **Optimal key idea:** length-prefix each string so any characters are safe (including delimiters).

### Approaches

1. **Bad (Join with simple delimiter)**
   - Fails if delimiter appears in data.

2. **Better (Escape delimiter + split)**
   - Works with careful escaping, but error-prone.

3. **Best (Length Prefix Encoding)**
   - Encode each string as `<len>#<content>`.
   - Decode by reading length then exact substring.
   - Time: `O(total_chars)`, Space: `O(total_chars)`.

---

## 7) Product of Array Except Self

- **Pattern:** Prefix/Suffix Products
- **Difficulty:** Medium
- **Optimal key idea:** compute prefix and suffix products without division.

### Approaches

1. **Bad (For each index, multiply all others)**
   - Time: `O(n^2)`, Space: `O(1)` extra.

2. **Better (Use Division with Zero Handling)**
   - Time: `O(n)`, but disallowed in many versions + tricky around zeros.

3. **Best (Prefix + Suffix Passes)**
   - First pass stores left product, second pass multiplies right product.
   - Time: `O(n)`, Space: `O(1)` extra excluding output.

---

## 8) Valid Sudoku

- **Pattern:** Hash Set Constraints
- **Difficulty:** Medium
- **Optimal key idea:** each row/col/box must have unique digits.

### Approaches

1. **Bad (Re-scan row/col/box for every filled cell)**
   - Repeated work, near `O(9^3)` style checks.

2. **Best (Three Hash-Set Collections)**
   - `rows[r]`, `cols[c]`, `boxes[b]` track seen digits.
   - If duplicate in any set, invalid.
   - Time: `O(81)` -> constant, Space: `O(81)` -> constant.

---

## 9) Longest Consecutive Sequence

- **Pattern:** Hash Set + Sequence Starts
- **Difficulty:** Medium
- **Optimal key idea:** only start counting at numbers where `num-1` is absent.

### Approaches

1. **Bad (Sort + scan)**
   - Time: `O(n log n)`.

2. **Best (Hash Set sequence expansion from starts)**
   - For each `num`, if `num-1` not in set, expand forward.
   - Every number expanded at most once across all sequences.
   - Time: `O(n)` average, Space: `O(n)`.

---

## Notes

- All implementations for each approach are in `solutions.py` with clear naming.
- Naming convention:
  - `_bad`: brute-force or intentionally suboptimal approach.
  - `_better`: intermediate improvement.
  - `_best`: optimal/common interview solution.
