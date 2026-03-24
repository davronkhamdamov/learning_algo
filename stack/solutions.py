"""Stack category solutions from bad -> best."""

from typing import List


# 1) VALID PARENTHESES

def is_valid_parentheses_bad(s: str) -> bool:
    prev = None
    cur = s

    while prev != cur:
        prev = cur
        cur = cur.replace("()", "").replace("[]", "").replace("{}", "")

    return cur == ""


def is_valid_parentheses_best(s: str) -> bool:
    close_for_open = {"(": ")", "[": "]", "{": "}"}
    stack: List[str] = []

    for ch in s:
        if ch in close_for_open:
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if close_for_open[top] != ch:
                return False

    return len(stack) == 0


# 2) MIN STACK

class MinStackBad:
    def __init__(self) -> None:
        self.vals: List[int] = []

    def push(self, val: int) -> None:
        self.vals.append(val)

    def pop(self) -> None:
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        best = self.vals[0]
        for v in self.vals:
            if v < best:
                best = v
        return best


class MinStackBest:
    def __init__(self) -> None:
        self.vals: List[int] = []
        self.mins: List[int] = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.vals.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# 3) EVALUATE REVERSE POLISH NOTATION

def eval_rpn_bad(tokens: List[str]) -> int:
    arr = tokens[:]
    ops = {"+", "-", "*", "/"}

    while len(arr) > 1:
        i = 0
        while i < len(arr):
            if arr[i] in ops:
                a = int(arr[i - 2])
                b = int(arr[i - 1])
                op = arr[i]

                if op == "+":
                    value = a + b
                elif op == "-":
                    value = a - b
                elif op == "*":
                    value = a * b
                else:
                    value = int(a / b)

                arr = arr[: i - 2] + [str(value)] + arr[i + 1 :]
                break
            i += 1

    return int(arr[0])


def eval_rpn_best(tokens: List[str]) -> int:
    stack: List[int] = []

    for tok in tokens:
        if tok not in {"+", "-", "*", "/"}:
            stack.append(int(tok))
            continue

        b = stack.pop()
        a = stack.pop()

        if tok == "+":
            stack.append(a + b)
        elif tok == "-":
            stack.append(a - b)
        elif tok == "*":
            stack.append(a * b)
        else:
            stack.append(int(a / b))

    return stack[0]


# 4) DAILY TEMPERATURES

def daily_temperatures_bad(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    ans = [0] * n

    for i in range(n):
        j = i + 1
        while j < n:
            if temperatures[j] > temperatures[i]:
                ans[i] = j - i
                break
            j += 1

    return ans


def daily_temperatures_best(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    ans = [0] * n
    stack: List[int] = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_i = stack.pop()
            ans[prev_i] = i - prev_i
        stack.append(i)

    return ans


# 5) CAR FLEET

def car_fleet_bad(target: int, position: List[int], speed: List[int]) -> int:
    # Very rough simulation approach (educational "bad" baseline)
    cars = [[p, s] for p, s in zip(position, speed)]
    if not cars:
        return 0

    # Simulate in integer time slices until all reach target.
    # This can be extremely slow for large values.
    fleets = len(cars)
    reached = [False] * len(cars)

    for _ in range(100000):
        if all(reached):
            break

        cars.sort(key=lambda x: x[0])

        for i in range(len(cars)):
            if cars[i][0] >= target:
                reached[i] = True
                continue
            cars[i][0] += cars[i][1]
            if cars[i][0] >= target:
                reached[i] = True

        for i in range(len(cars) - 1):
            if cars[i][0] >= cars[i + 1][0]:
                cars[i][0] = cars[i + 1][0]
                cars[i][1] = cars[i + 1][1]

    # Not mathematically exact for all cases; intentionally poor baseline.
    times = sorted((target - p) / s for p, s in zip(position, speed))
    # fallback count-ish approximation:
    return max(1, sum(1 for i in range(1, len(times)) if times[i] > times[i - 1]))


def car_fleet_best(target: int, position: List[int], speed: List[int]) -> int:
    pairs = sorted(zip(position, speed), reverse=True)
    stack: List[float] = []

    for p, s in pairs:
        arrival = (target - p) / s
        if stack and arrival <= stack[-1]:
            continue
        stack.append(arrival)

    return len(stack)


# 6) LARGEST RECTANGLE IN HISTOGRAM

def largest_rectangle_area_bad(heights: List[int]) -> int:
    n = len(heights)
    best = 0

    for i in range(n):
        min_h = heights[i]
        for j in range(i, n):
            min_h = min(min_h, heights[j])
            area = min_h * (j - i + 1)
            best = max(best, area)

    return best


def largest_rectangle_area_best(heights: List[int]) -> int:
    best = 0
    stack: List[tuple[int, int]] = []  # (start_index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            best = max(best, height * (i - idx))
            start = idx
        stack.append((start, h))

    n = len(heights)
    for idx, height in stack:
        best = max(best, height * (n - idx))

    return best
