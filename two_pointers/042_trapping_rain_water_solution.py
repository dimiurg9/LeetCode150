"""
42. Trapping Rain Water (Hard)

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The elevation map (black) is represented by the array.
    In this case, 6 units of rain water (blue) are being trapped.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    - n == height.length
    - 1 <= n <= 2 * 10^4
    - 0 <= height[i] <= 10^5
"""

# ==============================================================
# INTERVIEW PLAN
# ==============================================================
# 1. "Water at each index = min(max_left, max_right) - height[i]"
# 2. "Brute force: for each bar, scan left and right for max → O(n²)"
# 3. "Optimization 1: Precompute left_max[] and right_max[] arrays → O(n) time, O(n) space"
# 4. "Optimization 2: Two pointers — track left_max and right_max,
#     move the pointer on the smaller side inward. We only need the
#     min of the two maxes, and the smaller side guarantees correctness."
# 5. "Time: O(n), Space: O(1) for two-pointer; O(n) for prefix arrays"
# ==============================================================


# --------------------------------------------------------------
# SOLUTION 1: Two Pointers (BEST)
# Remember as: "Squeeze from both ends; move the shorter wall inward, accumulate water on that side."
# --------------------------------------------------------------
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


# --------------------------------------------------------------
# SOLUTION 2: Prefix Max Arrays (easy to remember)
# Remember as: "Build left_max[] and right_max[], then water[i] = min(L[i], R[i]) - h[i]."
# --------------------------------------------------------------
def trap_prefix(height):
    if not height:
        return 0
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


# ==============================================================
# TEST CASES
# ==============================================================
test_cases = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([], 0),
    ([3], 0),
    ([5,4,3,2,1], 0),
    ([1,2,3,4,5], 0),
    ([3,0,3], 3),
    ([2,0,2], 2),
]

print("--- Solution 1: Two Pointers ---")
for i, (height, expected) in enumerate(test_cases, 1):
    result = trap(height)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")

print("\n--- Solution 2: Prefix Max Arrays ---")
for i, (height, expected) in enumerate(test_cases, 1):
    result = trap_prefix(height)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")