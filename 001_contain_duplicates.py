"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.
"""

def contain_duplicates(nums):
    return len(nums) != len(set(nums))

def contain_duplicates_no_set(nums):
    result = []
    for i in nums:
        if i in result:
            return True
        result.append(i)
    return False

nums = [1,2,3,1]
result = contain_duplicates(nums)
print(result)

nums = [1,2,3]
result = contain_duplicates(nums)
print(result)

nums = [1,2,3,1]
result = contain_duplicates_no_set(nums)
print(result)

nums = [1,2,3]
result = contain_duplicates_no_set(nums)
print(result)