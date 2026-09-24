"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without
repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence
and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    pass

test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("dvdf", 3),
    ("abba", 2),
    ("tmmzuxt", 5),
]

for i, (s, expected) in enumerate(test_cases, 1):
    result = length_of_longest_substring(s)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")