"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The max area is between index 1 (height 8) and index 8 (height 7):
    min(8, 7) * (8 - 1) = 7 * 7 = 49.

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    - n == height.length
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4
"""

# ============================================================
# INTERVIEW PLAN
# ============================================================
# 1. "This is a two-pointer problem. Area = min(height[left], height[right]) * width."
# 2. "Start with widest container (pointers at both ends)."
# 3. "To possibly find a larger area, we must increase the height —
#     so we move the pointer pointing to the SHORTER line inward."
# 4. "Why? Moving the taller pointer can only decrease or maintain height
#     while always decreasing width — so area can never increase."
# 5. "Track the max area seen at each step."
#
# Time:  O(n) — each pointer moves at most n times total
# Space: O(1) — only a few variables
# ============================================================


# --------------------------------------------------
# SOLUTION 1: Two Pointers (BEST)
# Remember as: "Start wide, shrink from the short side."
# --------------------------------------------------
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# --------------------------------------------------
# SOLUTION 2: Brute Force (easy to remember)
# Remember as: "Try every pair, track the max."
# --------------------------------------------------
def max_area_brute(height: list[int]) -> int:
    max_water = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            width = j - i
            h = min(height[i], height[j])
            max_water = max(max_water, width * h)

    return max_water


# ============================================================
# TEST CASES
# ============================================================
test_cases = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([2, 3, 10, 5, 7, 8, 9], 36),
    ([1, 1, 1, 1, 1, 1], 5),
    ([1, 2, 3, 4, 5], 6),
    ([5, 1, 1, 1, 5], 20),
]

print("=== SOLUTION 1: Two Pointers ===")
for i, (height, expected) in enumerate(test_cases, 1):
    result = max_area(height)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")

print("\n=== SOLUTION 2: Brute Force ===")
for i, (height, expected) in enumerate(test_cases, 1):
    result = max_area_brute(height)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")