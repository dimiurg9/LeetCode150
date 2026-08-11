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


def trap(height):
    pass


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

for i, (height, expected) in enumerate(test_cases, 1):
    result = trap(height)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")