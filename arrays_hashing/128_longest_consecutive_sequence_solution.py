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


# ============================================================
# INTERVIEW PLAN (what to say out loud):
# ============================================================
# 1. "Sorting would give O(n log n). To get O(n), I'll use a HashSet."
#
# 2. "Key insight: I only want to START counting from the BEGINNING
#     of a sequence. A number is a sequence start if (num - 1) is
#     NOT in the set."
#
# 3. "For each sequence start, I count consecutive numbers going up
#     (num+1, num+2, ...) and track the max length."
#
# 4. "Even though there's a while loop inside a for loop, each number
#     is visited at most twice total → O(n)."
#
# Time: O(n)
# Space: O(n) for the set
# ============================================================


# ------------------------------
# SOLUTION 1: HashSet — find sequence starts (BEST & easy to remember)
# Remember: "Set it. No left neighbor? Count right."
# ------------------------------
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if this is the START of a sequence
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest


# ------------------------------
# SOLUTION 2: Sorting approach (simpler logic, but O(n log n))
# Use if you blank on the set trick — not optimal but shows thinking
# ------------------------------
def longest_consecutive_v2(nums):
    if not nums:
        return 0

    nums = sorted(set(nums))  # remove dupes + sort
    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest




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