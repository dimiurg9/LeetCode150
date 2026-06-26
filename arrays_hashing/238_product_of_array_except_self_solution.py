"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 
32-bit integer.

You must write an algorithm that runs in O(n) time and without using 
the division operator.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve it in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""


# ============================================================
# INTERVIEW PLAN (what to say out loud):
# ============================================================
# 1. "We can't use division, so I'll think about what info each
#     position needs: the product of everything to its LEFT and
#     the product of everything to its RIGHT."
#
# 2. "I'll do two passes:
#     - First pass (left to right): build prefix products
#     - Second pass (right to left): multiply by suffix products"
#
# 3. "For O(1) extra space, I'll use the output array itself to
#     store prefix products, then multiply in-place on the second pass."
#
# Time: O(n) — two passes
# Space: O(1) extra (output array doesn't count)
# ============================================================


# ------------------------------
# SOLUTION 1: Two-pass (BEST — O(n) time, O(1) extra space)
# Easy to remember: "prefix going right, suffix going left"
# ------------------------------
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Pass 1: fill answer[i] with product of all elements to the LEFT of i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Pass 2: multiply answer[i] by product of all elements to the RIGHT of i
    postfix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer


test_cases = [
    ([1, 2, 3, 4],        [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3],   [0, 0, 9, 0, 0]),
    ([2, 3],              [3, 2]),
    ([0, 0],              [0, 0]),
    ([1, 0, 3, 4],        [0, 12, 0, 0]),
    ([5, 1, 1, 1],        [1, 5, 5, 5]),
    ([-1, -1, -1, -1],    [-1, -1, -1, -1]),
]

for i, (nums, expected) in enumerate(test_cases, 1):
    result = product_except_self(nums)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")




# ------------------------------
# SOLUTION 2: Two separate arrays (easier to visualize, O(n) extra space)
# Good if you blank on the in-place trick
# ------------------------------
def product_except_self_v2(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n

    # Build left products: left[i] = product of nums[0..i-1]
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    # Build right products: right[i] = product of nums[i+1..n-1]
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # answer[i] = left[i] * right[i]
    return [left[i] * right[i] for i in range(n)]


