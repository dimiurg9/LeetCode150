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


def is_palindrome(s):
    pass




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