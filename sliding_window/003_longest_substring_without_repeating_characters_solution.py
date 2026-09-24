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

# INTERVIEW PLAN
# 1. Clarify: empty string returns 0, answer is a LENGTH not the substring.
# 2. State approach: sliding window with hashmap of char -> last index.
# 3. Explain: expand right pointer, if char seen inside window, jump left
#    past its last occurrence.
# 4. Track max window size as we go.
# 5. Complexity: Time O(n), Space O(min(n, charset)).


# SOLUTION 1: Sliding Window + HashMap (BEST)
# Remember as: "right expands, left jumps past repeat, track max."
def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


# SOLUTION 2: Brute Force Check All Substrings (easy to remember)
# Remember as: "try every start, grow until repeat."
def length_of_longest_substring_brute(s: str) -> int:
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best


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