"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

def two_sum(nums, t):
    pass




test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4],      6, [1, 2]),
    ([3, 3],         6, [0, 1]),
]

for i, (nums, target, expected) in enumerate(test_cases, 1):
    result = two_sum(nums, target)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")
        
# nums = [2,7,11,15]
# target = 9
# result = two_sum(nums, target)
# print(f"result: {result}, expected: [0,1]")

# assert two_sum([2,7,11,15], 9) == [0,1]
# assert two_sum([3,2,4], 6) == [1,2]
# assert two_sum([3,3], 6) == [0,1]