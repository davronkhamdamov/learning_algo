"""Two Pointers solutions from bad -> better -> best."""

from bisect import bisect_left
from typing import List


# 1) VALID PALINDROME

def is_palindrome_bad(s: str) -> bool:
    cleaned = []
    for ch in s:
        if ch.isalnum():
            cleaned.append(ch.lower())

    cleaned = "".join(cleaned)
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_best(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# 2) TWO SUM II (SORTED INPUT)

def two_sum_ii_bad(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []


def two_sum_ii_better(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        need = target - numbers[i]
        j = bisect_left(numbers, need, i + 1, n)
        if j < n and numbers[j] == need:
            return [i + 1, j + 1]
    return []


def two_sum_ii_best(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1

    return []


# 3) 3SUM

def three_sum_bad(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))

    return [list(triplet) for triplet in sorted(result)]


def three_sum_better(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    ans = set()

    for i in range(n):
        seen = set()
        for j in range(i + 1, n):
            need = -(nums[i] + nums[j])
            if need in seen:
                ans.add((nums[i], need, nums[j]))
            seen.add(nums[j])

    return [list(t) for t in sorted(ans)]


def three_sum_best(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result: List[List[int]] = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


# 4) CONTAINER WITH MOST WATER

def max_area_bad(height: List[int]) -> int:
    best = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            best = max(best, area)

    return best


def max_area_best(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        best = max(best, width * h)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return best


# 5) TRAPPING RAIN WATER

def trap_bad(height: List[int]) -> int:
    water = 0
    n = len(height)

    for i in range(n):
        left_max = 0
        right_max = 0

        for l in range(i, -1, -1):
            left_max = max(left_max, height[l])
        for r in range(i, n):
            right_max = max(right_max, height[r])

        water += min(left_max, right_max) - height[i]

    return water


def trap_better(height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


def trap_best(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water
