"""
LeetCode 74: Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix `matrix` with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return True if `target` is in `matrix` or False otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
  Output: True

Example 2:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
  Output: False

Constraints:
  m == matrix.length
  n == matrix[i].length
  1 <= m, n <= 100
  -10^4 <= matrix[i][j], target <= 10^4
"""

# INTERVIEW PLAN
# 1. Clarify: m x n matrix, rows sorted, first of row > last of prev row -> fully sorted if flattened.
# 2. State idea: treat matrix as a sorted 1D array of length m*n, binary search it.
# 3. Explain mapping: index mid -> row = mid // n, col = mid % n.
# 4. Edge cases: 1x1 matrix, target smaller than matrix[0][0], larger than matrix[-1][-1].
# 5. Code flattened binary search.
# 6. Mention alternative: staircase from top-right (simpler but O(m+n)).
# Time: O(log(m*n)) for BEST, Space: O(1)

# SOLUTION 1: Flattened Binary Search (BEST)
# Remember as: "Treat as 1D sorted array, mid -> [mid//n][mid%n]"
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


# SOLUTION 2: Staircase Search (easy to remember)
# Remember as: "Start top-right, go left if big, down if small"
def search_matrix_staircase(matrix, target):
    m, n = len(matrix), len(matrix[0])
    r, c = 0, n - 1
    while r < m and c >= 0:
        val = matrix[r][c]
        if val == target:
            return True
        elif val > target:
            c -= 1
        else:
            r += 1
    return False


test_cases = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([[1]], 1, True),
    ([[1]], 0, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1, True),
    ([[1, 3], [5, 7]], 4, False),
]

for i, (matrix, target, expected) in enumerate(test_cases, 1):
    result = search_matrix(matrix, target)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")