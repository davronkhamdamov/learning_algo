# Trees (Category 7)

This folder contains your seventh category: **Trees**.

Each problem is documented from **bad/brute-force** to **best/optimal** with pattern classification and complexity ideas.

- Implementations: `solutions.py`
- Explanations + classifications: this file

---

## Prerequisites

- **BST Insert and Remove** (Data Structures & Algorithms for Beginners)
- **Depth-First Search** (Data Structures & Algorithms for Beginners)
- **Breadth-First Search** (Data Structures & Algorithms for Beginners)
- **BST Sets and Maps** (Data Structures & Algorithms for Beginners)
- **Iterative DFS** (Advanced Algorithms)

---

## Problems Covered

1. Invert Binary Tree  
2. Maximum Depth of Binary Tree  
3. Diameter of Binary Tree  
4. Balanced Binary Tree  
5. Same Tree  
6. Subtree of Another Tree  
7. Lowest Common Ancestor of a Binary Search Tree  
8. Binary Tree Level Order Traversal  
9. Binary Tree Right Side View  
10. Count Good Nodes In Binary Tree  
11. Validate Binary Search Tree  
12. Kth Smallest Element In a BST  
13. Construct Binary Tree From Preorder And Inorder Traversal  
14. Binary Tree Maximum Path Sum  
15. Serialize And Deserialize Binary Tree

---

## Classification Summary

- **Core patterns:** DFS (recursive/iterative), BFS queue traversal, BST ordering constraints, tree construction from traversals, path/state propagation, and serialization.
- **Typical optimization direction:** avoid repeated subtree rescans (`O(n^2)`), use one-pass postorder/DFS/BFS (`O(n)`), and use hash maps for index lookups in reconstruction problems.

---

## Notes

- `solutions.py` uses:
  - `_bad` for baseline/brute-force where meaningful
  - `_best` for optimal/canonical interview implementations
- Includes `TreeNode`, plus `CodecBest` for serialization/deserialization.
