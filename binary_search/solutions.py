"""Binary Search category solutions from bad -> better -> best."""

from bisect import bisect_right
from collections import defaultdict
from typing import Dict, List, Tuple


# 1) BINARY SEARCH

def binary_search_bad(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


def binary_search_best(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 2) SEARCH A 2D MATRIX

def search_matrix_bad(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False


def search_matrix_better(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    for row in matrix:
        if row[0] <= target <= row[-1]:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

    return False


def search_matrix_best(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        r, c = divmod(mid, cols)
        value = matrix[r][c]

        if value == target:
            return True
        if value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 3) KOKO EATING BANANAS

def min_eating_speed_bad(piles: List[int], h: int) -> int:
    max_pile = max(piles)

    for speed in range(1, max_pile + 1):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        if hours <= h:
            return speed

    return max_pile


def min_eating_speed_best(piles: List[int], h: int) -> int:
    def can_finish(speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h

    left, right = 1, max(piles)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if can_finish(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


# 4) FIND MINIMUM IN ROTATED SORTED ARRAY

def find_min_bad(nums: List[int]) -> int:
    minimum = nums[0]
    for num in nums[1:]:
        if num < minimum:
            minimum = num
    return minimum


def find_min_best(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# 5) SEARCH IN ROTATED SORTED ARRAY

def search_rotated_bad(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


def search_rotated_best(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# 6) TIME BASED KEY VALUE STORE

class TimeMapBad:
    def __init__(self) -> None:
        self.store: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        best_time = -1
        best_value = ""
        for t, v in self.store[key]:
            if t <= timestamp and t > best_time:
                best_time = t
                best_value = v

        return best_value


class TimeMapBest:
    def __init__(self) -> None:
        self.store: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        entries = self.store[key]
        times = [t for t, _ in entries]
        idx = bisect_right(times, timestamp) - 1

        if idx < 0:
            return ""
        return entries[idx][1]


# 7) MEDIAN OF TWO SORTED ARRAYS

def find_median_sorted_arrays_bad(nums1: List[int], nums2: List[int]) -> float:
    merged = sorted(nums1 + nums2)
    n = len(merged)

    if n % 2 == 1:
        return float(merged[n // 2])
    return (merged[n // 2 - 1] + merged[n // 2]) / 2.0


def find_median_sorted_arrays_better(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)
    total = m + n
    median_pos_1 = (total - 1) // 2
    median_pos_2 = total // 2

    i = j = 0
    current_index = -1
    val1 = val2 = 0

    while i < m or j < n:
        if j >= n or (i < m and nums1[i] <= nums2[j]):
            cur = nums1[i]
            i += 1
        else:
            cur = nums2[j]
            j += 1

        current_index += 1
        if current_index == median_pos_1:
            val1 = cur
        if current_index == median_pos_2:
            val2 = cur
            break

    return (val1 + val2) / 2.0


def find_median_sorted_arrays_best(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    left, right = 0, x

    while left <= right:
        part_x = (left + right) // 2
        part_y = (x + y + 1) // 2 - part_x

        max_left_x = float("-inf") if part_x == 0 else nums1[part_x - 1]
        min_right_x = float("inf") if part_x == x else nums1[part_x]

        max_left_y = float("-inf") if part_y == 0 else nums2[part_y - 1]
        min_right_y = float("inf") if part_y == y else nums2[part_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            return float(max(max_left_x, max_left_y))

        if max_left_x > min_right_y:
            right = part_x - 1
        else:
            left = part_x + 1

    raise ValueError("Input arrays are not sorted or invalid")
