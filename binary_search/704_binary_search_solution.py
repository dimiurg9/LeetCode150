"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 10^4
    -10^4 < nums[i], target < 10^4
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""

# =============================================================================
# INTERVIEW PLAN — what to say out loud
# =============================================================================
# 1. Restate: "Sorted array, unique values, find the index of target, -1 if
#    missing. The O(log n) requirement means binary search, not a linear scan."
# 2. Clarify: "Always sorted ascending? Values unique? Can the array be empty?"
#    (Constraints say len >= 1, but I'll handle empty safely anyway.)
# 3. Core idea: keep a search window [lo, hi]. Look at the middle. If it equals
#    the target we're done. If it's too small, the answer can only be to the
#    right, so lo = mid + 1. If it's too big, hi = mid - 1. Each step halves
#    the window.
# 4. Name the three classic bugs and how I avoid them:
#       a) loop condition must be `while lo <= hi` (inclusive window), otherwise
#          a 1-element window is never checked.
#       b) must move past mid (mid + 1 / mid - 1), never lo = mid, or infinite loop.
#       c) use lo + (hi - lo) // 2 to show awareness of overflow in Java/C++
#          (Python ints are unbounded, so it's stylistic here).
# 5. Walk Example 2 to prove the -1 path: window shrinks until lo > hi, exit loop.
# 6. Complexity: Time O(log n) — window halves each iteration.
#                Space O(1) — two pointers, no extra storage.
#    (Mention the recursive variant is O(log n) space from the call stack.)
# 7. Test: found-in-middle, not-found, single element, both boundaries,
#    target below and above the whole range.


# =============================================================================
# SOLUTION 1: Iterative Two-Pointer Binary Search (BEST)
# Remember as: "Shrink an inclusive window [lo, hi] — while lo <= hi, jump past mid."
# Time: O(log n)   Space: O(1)
# =============================================================================
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:                      # inclusive window: must be <=
        mid = lo + (hi - lo) // 2        # overflow-safe midpoint
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1                 # answer is strictly right of mid
        else:
            hi = mid - 1                 # answer is strictly left of mid
    return -1


# =============================================================================
# SOLUTION 2: Recursive Binary Search (easy to remember)
# Remember as: "Same halving, but let the call stack hold lo and hi."
# Time: O(log n)   Space: O(log n) recursion stack
# =============================================================================
def search_recursive(nums, target):
    def helper(lo, hi):
        if lo > hi:                      # empty window -> not found
            return -1
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return helper(mid + 1, hi)
        return helper(lo, mid - 1)

    return helper(0, len(nums) - 1)


# =============================================================================
# SOLUTION 3 (bonus, one-liner to mention but NOT to submit): bisect
# Remember as: "bisect_left then confirm the hit."
# Time: O(log n)   Space: O(1)
# =============================================================================
# from bisect import bisect_left
# def search_bisect(nums, target):
#     i = bisect_left(nums, target)
#     return i if i < len(nums) and nums[i] == target else -1


test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),       # LC example 1
    ([-1, 0, 3, 5, 9, 12], 2, -1),      # LC example 2
    ([5], 5, 0),                        # single element, found
    ([5], -5, -1),                      # single element, not found
    ([1, 2, 3, 4, 5], 1, 0),            # first element (left boundary)
    ([1, 2, 3, 4, 5], 5, 4),            # last element (right boundary)
    ([2, 4, 6, 8], 1, -1),              # target below range, even length
    ([2, 4, 6, 8], 9, -1),              # target above range, even length
]

for i, (nums, target, expected) in enumerate(test_cases, 1):
    result = search(nums, target)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")