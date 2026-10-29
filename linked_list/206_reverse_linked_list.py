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


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next



def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    #  print all values

    # attach at head

    # attach at node

    


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