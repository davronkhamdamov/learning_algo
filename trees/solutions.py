"""Trees category solutions from bad -> best."""

from __future__ import annotations

from collections import deque
from typing import Dict, List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


# 1) INVERT BINARY TREE

def invert_tree_bad(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    new_root = TreeNode(root.val)
    new_root.left = invert_tree_bad(root.right)
    new_root.right = invert_tree_bad(root.left)
    return new_root


def invert_tree_best(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree_best(root.left)
    invert_tree_best(root.right)
    return root


# 2) MAXIMUM DEPTH OF BINARY TREE

def max_depth_bad(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([(root, 1)])
    ans = 0
    while q:
        node, depth = q.popleft()
        ans = max(ans, depth)
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return ans


def max_depth_best(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth_best(root.left), max_depth_best(root.right))


# 3) DIAMETER OF BINARY TREE

def diameter_of_binary_tree_bad(root: Optional[TreeNode]) -> int:
    def depth(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(depth(node.left), depth(node.right))

    if not root:
        return 0

    left_d = diameter_of_binary_tree_bad(root.left)
    right_d = diameter_of_binary_tree_bad(root.right)
    through = depth(root.left) + depth(root.right)

    return max(left_d, right_d, through)


def diameter_of_binary_tree_best(root: Optional[TreeNode]) -> int:
    best = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0

        l = dfs(node.left)
        r = dfs(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    dfs(root)
    return best


# 4) BALANCED BINARY TREE

def is_balanced_bad(root: Optional[TreeNode]) -> bool:
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    if not root:
        return True

    return (
        abs(height(root.left) - height(root.right)) <= 1
        and is_balanced_bad(root.left)
        and is_balanced_bad(root.right)
    )


def is_balanced_best(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        l = dfs(node.left)
        if l == -1:
            return -1
        r = dfs(node.right)
        if r == -1:
            return -1

        if abs(l - r) > 1:
            return -1
        return 1 + max(l, r)

    return dfs(root) != -1


# 5) SAME TREE

def is_same_tree_bad(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def preorder(node: Optional[TreeNode], out: List[Optional[int]]) -> None:
        if not node:
            out.append(None)
            return
        out.append(node.val)
        preorder(node.left, out)
        preorder(node.right, out)

    a, b = [], []
    preorder(p, a)
    preorder(q, b)
    return a == b


def is_same_tree_best(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree_best(p.left, q.left) and is_same_tree_best(p.right, q.right)


# 6) SUBTREE OF ANOTHER TREE

def is_subtree_bad(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    def serialize(node: Optional[TreeNode], out: List[str]) -> None:
        if not node:
            out.append('#')
            return
        out.append(f"{node.val},")
        serialize(node.left, out)
        serialize(node.right, out)

    a, b = [], []
    serialize(root, a)
    serialize(sub_root, b)
    return ''.join(b) in ''.join(a)


def is_subtree_best(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)

    if not sub_root:
        return True
    if not root:
        return False
    if same(root, sub_root):
        return True

    return is_subtree_best(root.left, sub_root) or is_subtree_best(root.right, sub_root)


# 7) LOWEST COMMON ANCESTOR OF A BST

def lowest_common_ancestor_bst_bad(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    path = []

    def dfs(node: Optional[TreeNode], target: int) -> bool:
        if not node:
            return False
        path.append(node)
        if node.val == target:
            return True
        if dfs(node.left, target) or dfs(node.right, target):
            return True
        path.pop()
        return False

    path_p, path_q = [], []
    path.clear(); dfs(root, p.val); path_p = path[:]
    path.clear(); dfs(root, q.val); path_q = path[:]

    i = 0
    ans = None
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        ans = path_p[i]
        i += 1

    return ans


def lowest_common_ancestor_bst_best(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    cur = root

    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur

    return None


# 8) BINARY TREE LEVEL ORDER TRAVERSAL

def level_order_bad(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    levels: Dict[int, List[int]] = {}

    def dfs(node: Optional[TreeNode], depth: int) -> None:
        if not node:
            return
        levels.setdefault(depth, []).append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return [levels[d] for d in sorted(levels)]


def level_order_best(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)

    return result


# 9) BINARY TREE RIGHT SIDE VIEW

def right_side_view_bad(root: Optional[TreeNode]) -> List[int]:
    levels = level_order_best(root)
    return [level[-1] for level in levels if level]


def right_side_view_best(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


# 10) COUNT GOOD NODES IN BINARY TREE

def good_nodes_bad(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode], path: List[int]) -> int:
        if not node:
            return 0

        current_good = 1 if node.val >= max(path) else 0
        path.append(node.val)
        total = current_good + dfs(node.left, path) + dfs(node.right, path)
        path.pop()
        return total

    if not root:
        return 0
    return dfs(root, [root.val])


def good_nodes_best(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
        if not node:
            return 0

        good = 1 if node.val >= max_so_far else 0
        max_so_far = max(max_so_far, node.val)

        return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

    if not root:
        return 0
    return dfs(root, root.val)


# 11) VALIDATE BST

def is_valid_bst_bad(root: Optional[TreeNode]) -> bool:
    vals = []

    def inorder(node: Optional[TreeNode]) -> None:
        if not node:
            return
        inorder(node.left)
        vals.append(node.val)
        inorder(node.right)

    inorder(root)
    return all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))


def is_valid_bst_best(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float('-inf'), float('inf'))


# 12) KTH SMALLEST ELEMENT IN BST

def kth_smallest_bad(root: Optional[TreeNode], k: int) -> int:
    vals = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        vals.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    vals.sort()
    return vals[k - 1]


def kth_smallest_best(root: Optional[TreeNode], k: int) -> int:
    stack = []
    cur = root

    while True:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right


# 13) CONSTRUCT TREE FROM PREORDER AND INORDER

def build_tree_bad(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    idx = inorder.index(root_val)

    root = TreeNode(root_val)
    root.left = build_tree_bad(preorder[1 : 1 + idx], inorder[:idx])
    root.right = build_tree_bad(preorder[1 + idx :], inorder[idx + 1 :])
    return root


def build_tree_best(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    idx_map = {v: i for i, v in enumerate(inorder)}
    pre_idx = 0

    def helper(left: int, right: int) -> Optional[TreeNode]:
        nonlocal pre_idx
        if left > right:
            return None

        root_val = preorder[pre_idx]
        pre_idx += 1

        root = TreeNode(root_val)
        split = idx_map[root_val]
        root.left = helper(left, split - 1)
        root.right = helper(split + 1, right)
        return root

    return helper(0, len(inorder) - 1)


# 14) BINARY TREE MAXIMUM PATH SUM

def max_path_sum_bad(root: Optional[TreeNode]) -> int:
    # Naive: evaluate all root-to-node sums and combine; misses many cases but baseline example.
    best = float('-inf')

    def dfs(node: Optional[TreeNode], run_sum: int) -> None:
        nonlocal best
        if not node:
            return
        run_sum += node.val
        best = max(best, run_sum)
        dfs(node.left, run_sum)
        dfs(node.right, run_sum)

    dfs(root, 0)
    return int(best)


def max_path_sum_best(root: Optional[TreeNode]) -> int:
    best = float('-inf')

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        current_path = node.val + left_gain + right_gain
        best = max(best, current_path)

        return node.val + max(left_gain, right_gain)

    dfs(root)
    return int(best)


# 15) SERIALIZE AND DESERIALIZE BINARY TREE

class CodecBest:
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque(data.split(','))

        def dfs() -> Optional[TreeNode]:
            if not vals:
                return None
            v = vals.popleft()
            if v == '#':
                return None

            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
