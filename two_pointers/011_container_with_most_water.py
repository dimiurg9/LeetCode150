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


def max_area(height: list[int]) -> int:
    pass

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

for i, (height, expected) in enumerate(test_cases, 1):
    result = max_area(height)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")