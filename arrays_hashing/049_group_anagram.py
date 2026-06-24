"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

def group_anagrams(strs):
    pass


# --- Test Cases ---
test_cases = [
    (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]]),
    (["ab","ba","abc","cba","bac","xyz"], [["ab","ba"],["abc","cba","bac"],["xyz"]]),
    (["",""], [["",""]]),
    (["a","b","c"], [["a"],["b"],["c"]]),
]

for i, (strs, expected) in enumerate(test_cases, 1):
    result = group_anagrams(strs)
    # Sort inner lists and outer list for comparison (order doesn't matter)
    result_sorted = sorted([sorted(group) for group in result])
    expected_sorted = sorted([sorted(group) for group in expected])
    if result_sorted == expected_sorted:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")


