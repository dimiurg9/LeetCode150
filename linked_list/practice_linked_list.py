"""Practice file: linked list basics. Fill each TODO, then run: python practice_linked_list.py"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --- helpers (already done, don't touch) ---
def from_list(items):
    dummy = ListNode()
    cur = dummy
    for x in items:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


def show(label, head):
    print(f"{label}: {to_list(head)}")


# --- YOUR TURNS (fill in the pass blocks) ---

def attach_head(head, val):
    # TODO: make a new node with val, wire it before head, return new head
    new_node = ListNode(val)
    new_node.next = head
    head = new_node


def attach_middle(node, val):
    # TODO: insert val AFTER the given node. Return nothing.
    # node is some middle box you already hold (NOT head itself).
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node


def attach_tail(head, val):
    # TODO: walk to the last node, append val there. Return head.
    # Edge: if head is None, return ListNode(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = ListNode(val)


def delete_head(head):
    # TODO: drop the first node, return the new head.
    # Edge: if head is None, return None
    head = head.next


def delete_after(node):
    # TODO: skip over node.next (delete the box after node). Return nothing.
    # Edge: if node is None or node.next is None, do nothing
    


def delete_value(head, target):
    # TODO: delete ALL nodes with val == target. Return (possibly new) head.
    # Hint: use a dummy node so head-deletion needs no special case.
    pass


def get_value_at(head, index):
    # TODO: walk index steps, return curr.val. Return None if out of range.
    pass


# --- driver: sends lists into your methods and prints results ---
if __name__ == "__main__":
    print("=== 1. attach_head: put 0 in front of [1, 2, 3] ===")
    head = from_list([1, 2, 3])
    head = attach_head(head, 0)
    show("expected [0, 1, 2, 3], got", head)

    print("\n=== 2. attach_middle: put 15 after node 10 in [10, 20, 30] ===")
    head = from_list([10, 20, 30])
    node = head  # node holds the [10] box
    attach_middle(node, 15)
    show("expected [10, 15, 20, 30], got", head)

    print("\n=== 3. attach_tail: put 99 at end of [1, 2] ===")
    head = from_list([1, 2])
    head = attach_tail(head, 99)
    show("expected [1, 2, 99], got", head)

    print("\n=== 4. delete_head: drop first of [5, 6, 7] ===")
    head = from_list([5, 6, 7])
    head = delete_head(head)
    show("expected [6, 7], got", head)

    print("\n=== 5. delete_after: hold 10, delete what follows in [10, 20, 30] ===")
    head = from_list([10, 20, 30])
    delete_after(head)  # head IS the [10] box here
    show("expected [10, 30], got", head)

    print("\n=== 6. delete_value: remove all 1s from [1, 1, 2, 1, 3] ===")
    head = from_list([1, 1, 2, 1, 3])
    head = delete_value(head, 1)
    show("expected [2, 3], got", head)

    print("\n=== 7. get_value_at: index 2 of [10, 20, 30, 40] ===")
    head = from_list([10, 20, 30, 40])
    print("expected 30, got", get_value_at(head, 2))