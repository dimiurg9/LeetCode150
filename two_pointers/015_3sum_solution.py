"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = [0,1,1]
    Output: []

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]

Constraints:
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""

# ============================================================
# INTERVIEW PLAN
# ============================================================
# 1. "I'll sort the array first — this lets me use two pointers
#     and easily skip duplicates."
# 2. "I fix one element with index i, then use left/right pointers
#     on the remaining subarray to find pairs that sum to -nums[i]."
# 3. "To avoid duplicate triplets: skip duplicate values for i,
#     and after finding a valid triplet, skip duplicates for left and right."
# 4. "Early termination: if nums[i] > 0, no valid triplet is possible
#     since all remaining numbers are also positive."
#
# Time Complexity:  O(n²) — outer loop O(n) × two-pointer O(n)
# Space Complexity: O(1) extra (excluding output and sort space)
# ============================================================


# --------------------------------------------------
# SOLUTION 1: Sort + Two Pointers (BEST)
# --------------------------------------------------
# Remember as: "Sort, fix one, squeeze two pointers inward, skip dupes."

def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Early termination — smallest remaining number is positive
        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


# --------------------------------------------------
# SOLUTION 2: Sort + HashSet Two-Sum (easy to remember)
# --------------------------------------------------
# Remember as: "Sort, fix one, use a set to find the complement."

def three_sum_hashset(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], complement, nums[j]])
                # Skip duplicates for j
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

    return result


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

print("=== Solution 1: Sort + Two Pointers ===")
for i, (nums, expected) in enumerate(test_cases, 1):
    result = three_sum(list(nums))
    result_sorted = sorted([sorted(t) for t in result])
    expected_sorted = sorted([sorted(t) for t in expected])
    if result_sorted == expected_sorted:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result_sorted}, expected {expected_sorted}")

print("\n=== Solution 2: Sort + HashSet ===")
for i, (nums, expected) in enumerate(test_cases, 1):
    result = three_sum_hashset(list(nums))
    result_sorted = sorted([sorted(t) for t in result])
    expected_sorted = sorted([sorted(t) for t in expected])
    if result_sorted == expected_sorted:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result_sorted}, expected {expected_sorted}")