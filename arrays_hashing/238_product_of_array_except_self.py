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


def product_except_self(nums):
    pass
        



    
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