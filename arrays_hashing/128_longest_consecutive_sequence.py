"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""


def longest_consecutive(nums):
    pass

test_cases = [
    ([100, 4, 200, 1, 3, 2],          4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],  9),
    ([],                                0),
    ([1],                               1),
    ([1, 2, 0, 1],                      3),
    ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
    ([1, 1, 1, 1],                      1),
    ([-3, -2, -1, 0, 1],               5),
]

for i, (nums, expected) in enumerate(test_cases, 1):
    result = longest_consecutive(nums)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")