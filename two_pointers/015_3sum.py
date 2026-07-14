"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
                 nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
                 nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
                 The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    pass


# --- Test Cases ---
test_cases = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ([-1, 0, 1, 0], [[-1, 0, 1]]),
    ([1, 2, -2, -1], []),
    ([0, 0, 0, 0], [[0, 0, 0]]),
]

for i, (nums, expected) in enumerate(test_cases, 1):
    result = three_sum(nums)
    # Sort inner lists and outer list for order-independent comparison
    result_sorted = sorted([sorted(t) for t in result])
    expected_sorted = sorted([sorted(t) for t in expected])
    if result_sorted == expected_sorted:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result_sorted}, expected {expected_sorted}")