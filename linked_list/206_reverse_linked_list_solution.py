"""
LeetCode 206: Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]

Example 2:
  Input: head = [1,2]
  Output: [2,1]

Example 3:
  Input: head = []
  Output: []

Constraints:
  - The number of nodes in the list is the range [0, 5000].
  - -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------- INTERVIEW PLAN ----------------
# 1. Clarify: empty list -> return None; single node -> return as-is.
# 2. Say: "I'll do iterative in-place reversal with three pointers."
# 3. Walk through [1,2,3]: prev=None, curr=1 -> flip each arrow forward.
# 4. Code the loop: save nxt, point curr.next to prev, advance prev/curr.
# 5. Mention recursive alternative, then state complexity.
# Time: O(n) — visit each node once. Space: O(1) iterative / O(n) recursive.
# ------------------------------------------------

# SOLUTION 1: Iterative Three-Pointer (BEST)
# Remember as: "save next, flip, step forward"
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next  # save next
        curr.next = prev  # flip arrow
        prev = curr  # step forward
        curr = nxt
    return prev


# SOLUTION 2: Recursive (easy to remember)
# Remember as: "reverse the rest, then hang head at the end"
def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# --- helpers (not part of the interview solution, just for testing) ---
def to_linked_list(items):
    dummy = ListNode()
    cur = dummy
    for x in items:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


test_cases = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [3, 2, 1]),
    ([10, 20, 30, 40], [40, 30, 20, 10]),
]

for i, (inputs, expected) in enumerate(test_cases, 1):
    result = to_list(reverse_list(to_linked_list(inputs)))
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")