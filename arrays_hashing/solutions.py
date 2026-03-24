"""Arrays & Hashing solutions from bad -> best.

Each problem includes multiple implementations to show progression:
- *_bad: brute-force or intentionally weak approach
- *_better: improved but not optimal
- *_best: common optimal interview approach
"""

from collections import Counter, defaultdict
from typing import Dict, List, Tuple


# 1) CONTAINS DUPLICATE

def contains_duplicate_bad(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate_better(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False

    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            return True
    return False


def contains_duplicate_best(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# 2) VALID ANAGRAM

def is_anagram_bad(s: str, t: str) -> bool:
    """Still very slow style: remove matching chars from a mutable list.

    This avoids full permutation explosion but is intentionally inefficient:
    O(n^2) because each membership/removal can be linear.
    """
    if len(s) != len(t):
        return False

    t_chars = list(t)
    for ch in s:
        if ch not in t_chars:
            return False
        t_chars.remove(ch)
    return len(t_chars) == 0


def is_anagram_better(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def is_anagram_best(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq: Dict[str, int] = defaultdict(int)
    for ch in s:
        freq[ch] += 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return all(count == 0 for count in freq.values())


# 3) TWO SUM

def two_sum_bad(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_better(nums: List[int], target: int) -> List[int]:
    indexed = [(num, idx) for idx, num in enumerate(nums)]
    indexed.sort(key=lambda x: x[0])

    left, right = 0, len(indexed) - 1
    while left < right:
        total = indexed[left][0] + indexed[right][0]
        if total == target:
            return [indexed[left][1], indexed[right][1]]
        if total < target:
            left += 1
        else:
            right -= 1

    return []


def two_sum_best(nums: List[int], target: int) -> List[int]:
    seen: Dict[int, int] = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
    return []


# 4) GROUP ANAGRAMS

def group_anagrams_bad(strs: List[str]) -> List[List[str]]:
    groups: List[List[str]] = []
    for word in strs:
        placed = False
        sorted_word = sorted(word)

        for group in groups:
            if sorted(group[0]) == sorted_word:
                group.append(word)
                placed = True
                break

        if not placed:
            groups.append([word])

    return groups


def group_anagrams_better(strs: List[str]) -> List[List[str]]:
    groups: Dict[str, List[str]] = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


def group_anagrams_best(strs: List[str]) -> List[List[str]]:
    groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())


# 5) TOP K FREQUENT ELEMENTS

def top_k_frequent_bad(nums: List[int], k: int) -> List[int]:
    freq: Dict[int, int] = Counter(nums)
    result: List[int] = []

    for _ in range(k):
        best_num = None
        best_count = -1
        for num, count in freq.items():
            if count > best_count and num not in result:
                best_num = num
                best_count = count
        if best_num is not None:
            result.append(best_num)

    return result


def top_k_frequent_better(nums: List[int], k: int) -> List[int]:
    freq: Dict[int, int] = Counter(nums)
    pairs = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return [num for num, _ in pairs[:k]]


def top_k_frequent_best(nums: List[int], k: int) -> List[int]:
    freq: Dict[int, int] = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result: List[int] = []
    for count in range(len(buckets) - 1, 0, -1):
        for num in buckets[count]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# 6) ENCODE AND DECODE STRINGS

class CodecBad:
    """Unsafe delimiter-based codec (for demonstration only)."""

    def encode(self, strs: List[str]) -> str:
        return "|".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.split("|")


class CodecBest:
    """Length-prefixed codec: <len>#<string> for each entry."""

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        result: List[str] = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end

        return result


# 7) PRODUCT OF ARRAY EXCEPT SELF

def product_except_self_bad(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        answer[i] = prod
    return answer


def product_except_self_better(nums: List[int]) -> List[int]:
    total_product = 1
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num

    result = []
    for num in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            result.append(total_product if num == 0 else 0)
        else:
            result.append(total_product // num)

    return result


def product_except_self_best(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


# 8) VALID SUDOKU

def is_valid_sudoku_bad(board: List[List[str]]) -> bool:
    def is_duplicate(values: List[str]) -> bool:
        digits = [v for v in values if v != "."]
        return len(digits) != len(set(digits))

    for r in range(9):
        if is_duplicate(board[r]):
            return False

    for c in range(9):
        col = [board[r][c] for r in range(9)]
        if is_duplicate(col):
            return False

    for sr in range(0, 9, 3):
        for sc in range(0, 9, 3):
            box = []
            for r in range(sr, sr + 3):
                for c in range(sc, sc + 3):
                    box.append(board[r][c])
            if is_duplicate(box):
                return False

    return True


def is_valid_sudoku_best(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue

            box_id = (r // 3) * 3 + (c // 3)

            if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                return False

            rows[r].add(val)
            cols[c].add(val)
            boxes[box_id].add(val)

    return True


# 9) LONGEST CONSECUTIVE SEQUENCE

def longest_consecutive_bad(nums: List[int]) -> int:
    if not nums:
        return 0

    nums = sorted(set(nums))
    best = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            best = max(best, current)
            current = 1

    return max(best, current)


def longest_consecutive_best(nums: List[int]) -> int:
    num_set = set(nums)
    best = 0

    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)

    return best
