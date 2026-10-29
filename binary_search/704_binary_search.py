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


# def search(nums, target):
#     pass


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