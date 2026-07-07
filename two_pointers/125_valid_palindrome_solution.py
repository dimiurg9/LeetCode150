"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters 
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric 
characters. Since an empty string reads the same forward and backward, 
it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""


# ============================================================
# INTERVIEW PLAN (what to say out loud):
# ============================================================
# 1. "I need to compare the string ignoring non-alphanumeric chars
#     and case. Two approaches:"
#
# 2. "Option A: Clean the string first, then compare to its reverse."
#
# 3. "Option B (optimal): Two pointers from both ends. Skip non-alnum
#     chars, compare lowercase. No extra string needed."
#
# Time: O(n)
# Space: O(1) for two-pointer, O(n) for clean+reverse
# ============================================================


# ------------------------------
# SOLUTION 1: Two Pointers (BEST — O(n) time, O(1) space)
# Remember: "Left and right pointers, skip junk, compare lowercase"
# ------------------------------
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from the right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ------------------------------
# SOLUTION 2: Clean + Reverse (easiest to remember — O(n) space)
# Remember: "Filter, lowercase, compare to reverse"
# ------------------------------
def is_palindrome_v2(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


# ------------------------------
# SOLUTION 3: Clean + Two Pointer (middle ground)
# ------------------------------
def is_palindrome_v3(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True




test_cases = [
    ("A man, a plan, a canal: Panama",  True),
    ("race a car",                       False),
    (" ",                                True),
    ("",                                 True),
    ("a",                                True),
    ("ab",                               False),
    ("0P",                               False),
    (".,",                               True),
    ("aa",                               True),
    ("Race1a1ecaR",                      True),
]

for i, (s, expected) in enumerate(test_cases, 1):
    result = is_palindrome(s)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")