"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'
"""

# ============================================================
# INTERVIEW PLAN
# ============================================================
# 1. "I'll use a stack. When I see an opening bracket, I push it.
#     When I see a closing bracket, I check if the top of the stack
#     matches — if not, it's invalid."
# 2. "I'll use a hashmap to pair closing → opening brackets for
#     clean O(1) lookups."
# 3. "At the end, the stack must be empty — otherwise there are
#     unmatched opening brackets."
# 4. "Edge cases: single character → always False; all openers → False."
#
# Time:  O(n) — single pass through string
# Space: O(n) — stack can hold up to n/2 opening brackets
# ============================================================


# --------------------------------------------------
# SOLUTION 1: Stack + Hashmap (BEST)
# --------------------------------------------------
# Remember as: "Close maps to open; push openers, pop on closers, check match."

def is_valid(s: str) -> bool:
    stack = []
    close_to_open = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in close_to_open:
            # It's a closing bracket
            if not stack or stack[-1] != close_to_open[char]:
                return False
            stack.pop()
        else:
            # It's an opening bracket
            stack.append(char)

    return len(stack) == 0


# --------------------------------------------------
# SOLUTION 2: String Replacement (easy to remember)
# --------------------------------------------------
# Remember as: "Keep replacing '()' '{}' '[]' until nothing left."

def is_valid_replace(s: str) -> bool:
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return s == ''


# ============================================================
# TEST CASES
# ============================================================
test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False),
    ("{[]}", True),
    ("(", False),
    ("]", False),
]

print("=== SOLUTION 1: Stack + Hashmap ===")
for i, (s, expected) in enumerate(test_cases, 1):
    result = is_valid(s)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")

print("\n=== SOLUTION 2: String Replacement ===")
for i, (s, expected) in enumerate(test_cases, 1):
    result = is_valid_replace(s)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")