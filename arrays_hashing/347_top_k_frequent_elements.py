"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

def top_k_frequent(nums, k):
    counts = {}
    for i in nums:
        counts[i] = counts.get(i, 0) + 1

    buckets = [[] for i in range(len(nums) + 1)]

    for i, freq in counts.items():
        buckets[freq].append(i)

    result = []
    for i in range(len(buckets) -1, 0, -1):
        for items in buckets[i]:
            result.append(items)
            if len(result) == k:
                return result
            
    return result




test_cases = [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 2, 3, 4, 4, 4, 3, 3], 2, [3, 4]),
    ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
    ([5, 5, 5, 5, 1, 1, 1, 2, 2, 3], 3, [5, 1, 2]),
]

for i, (nums, k, expected) in enumerate(test_cases, 1):
    result = top_k_frequent(nums, k)
    if sorted(result) == sorted(expected):
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")