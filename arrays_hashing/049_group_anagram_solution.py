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

defaultdict(list) is a dictionary that automatically creates an empty list [] when you access a key that doesn't exist yet.

tuple(...) — converts the list to a tuple

tuple(['a', 'e', 't'])  # → ('a', 'e', 't')
Why tuple? Because dictionary keys must be hashable (immutable). Lists are mutable → can't be keys. Tuples are immutable → valid keys.

defaultdict(list) means: "for every new key, start with an empty [] so I can .append() strings into it."
# We want this result:
{
    ('a','e','t'): ["eat", "tea", "ate"],  # ← a list of grouped anagrams

"""

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)

    return list(groups.values())



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


