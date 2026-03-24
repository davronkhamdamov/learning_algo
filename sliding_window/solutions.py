"""Sliding Window category solutions from bad -> better -> best."""

from collections import Counter, defaultdict, deque
from typing import Dict, List


# 1) BEST TIME TO BUY AND SELL STOCK

def max_profit_bad(prices: List[int]) -> int:
    best = 0
    n = len(prices)

    for buy in range(n):
        for sell in range(buy + 1, n):
            best = max(best, prices[sell] - prices[buy])

    return best


def max_profit_best(prices: List[int]) -> int:
    min_price = float("inf")
    best = 0

    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)

    return best


# 2) LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

def length_of_longest_substring_bad(s: str) -> int:
    best = 0

    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)

    return best


def length_of_longest_substring_best(s: str) -> int:
    last_idx: Dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_idx and last_idx[ch] >= left:
            left = last_idx[ch] + 1

        last_idx[ch] = right
        best = max(best, right - left + 1)

    return best


# 3) LONGEST REPEATING CHARACTER REPLACEMENT

def character_replacement_bad(s: str, k: int) -> int:
    best = 0
    n = len(s)

    for i in range(n):
        freq: Dict[str, int] = defaultdict(int)
        max_freq = 0
        for j in range(i, n):
            freq[s[j]] += 1
            max_freq = max(max_freq, freq[s[j]])
            window_len = j - i + 1
            if window_len - max_freq <= k:
                best = max(best, window_len)

    return best


def character_replacement_best(s: str, k: int) -> int:
    counts: Dict[str, int] = defaultdict(int)
    left = 0
    max_count = 0
    best = 0

    for right, ch in enumerate(s):
        counts[ch] += 1
        max_count = max(max_count, counts[ch])

        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


# 4) PERMUTATION IN STRING

def check_inclusion_bad(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if m > n:
        return False

    sorted_s1 = sorted(s1)
    for i in range(n - m + 1):
        if sorted(s2[i : i + m]) == sorted_s1:
            return True

    return False


def check_inclusion_better(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if m > n:
        return False

    need = [0] * 26
    for ch in s1:
        need[ord(ch) - ord("a")] += 1

    window = [0] * 26
    for i in range(m):
        window[ord(s2[i]) - ord("a")] += 1

    if window == need:
        return True

    for r in range(m, n):
        window[ord(s2[r]) - ord("a")] += 1
        window[ord(s2[r - m]) - ord("a")] -= 1
        if window == need:
            return True

    return False


def check_inclusion_best(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if m > n:
        return False

    need = [0] * 26
    window = [0] * 26

    for ch in s1:
        need[ord(ch) - ord("a")] += 1
    for i in range(m):
        window[ord(s2[i]) - ord("a")] += 1

    matches = sum(1 for i in range(26) if need[i] == window[i])

    left = 0
    for right in range(m, n):
        if matches == 26:
            return True

        in_idx = ord(s2[right]) - ord("a")
        out_idx = ord(s2[left]) - ord("a")
        left += 1

        window[in_idx] += 1
        if window[in_idx] == need[in_idx]:
            matches += 1
        elif window[in_idx] - 1 == need[in_idx]:
            matches -= 1

        window[out_idx] -= 1
        if window[out_idx] == need[out_idx]:
            matches += 1
        elif window[out_idx] + 1 == need[out_idx]:
            matches -= 1

    return matches == 26


# 5) MINIMUM WINDOW SUBSTRING

def min_window_bad(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    best = ""

    for i in range(len(s)):
        freq: Dict[str, int] = defaultdict(int)
        for j in range(i, len(s)):
            freq[s[j]] += 1
            if all(freq[ch] >= cnt for ch, cnt in need.items()):
                candidate = s[i : j + 1]
                if best == "" or len(candidate) < len(best):
                    best = candidate
                break

    return best


def min_window_best(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    have = defaultdict(int)
    required = len(need)
    formed = 0

    left = 0
    best_len = float("inf")
    best_l = 0

    for right, ch in enumerate(s):
        have[ch] += 1

        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_l = left

            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1

    if best_len == float("inf"):
        return ""
    return s[best_l : best_l + best_len]


# 6) SLIDING WINDOW MAXIMUM

def max_sliding_window_bad(nums: List[int], k: int) -> List[int]:
    if not nums or k == 0:
        return []

    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i : i + k]))

    return result


def max_sliding_window_best(nums: List[int], k: int) -> List[int]:
    if not nums or k == 0:
        return []

    dq = deque()  # stores indices, values decreasing
    result = []

    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
