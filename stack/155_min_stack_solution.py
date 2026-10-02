"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:
  - MinStack() initializes the stack object.
  - void push(int val) pushes the element val onto the stack.
  - void pop() removes the element on the top of the stack.
  - int top() gets the top element of the stack.
  - int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
  Input:
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]
  Output: [null,null,null,null,-3,null,0,-2]
  Explanation:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2

Constraints:
  -2^31 <= val <= 2^31 - 1
  Methods pop, top and getMin operations will always be called on non-empty stacks.
  At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Harness note:
  min_stack_operations(operations, args) replays the call sequence and returns a
  list of results, using None for the constructor and for void calls
  (push / pop), mirroring LeetCode's `null`.
"""

# =============================================================================
# INTERVIEW PLAN — what to say out loud
# =============================================================================
# 1. Restate: "A normal stack already gives me O(1) push/pop/top. The only hard
#    part is getMin in O(1) — scanning the stack would be O(n)."
# 2. Name the blocker: "The minimum changes as elements leave, so I can't keep a
#    single min variable — once I pop the minimum, I've lost the previous one."
# 3. Key insight: "The history of minimums is itself a stack. Every value I push
#    has a 'minimum so far at this depth', and that value is restored exactly
#    when I pop back to that depth. So I store the min alongside the data."
# 4. Propose Solution 1: push (val, min_so_far) pairs into ONE stack.
#    getMin = peek the second slot of the top pair. Everything is O(1).
# 5. Mention the duplicate trap: "If I kept a separate min-stack with strict <,
#    pushing 2 twice then popping once would wrongly drop the min. Pairs make
#    that bug impossible — each element carries its own answer."
# 6. Edge cases to call out: single element; emptied-then-refilled stack (no
#    stale min); all-equal values; strictly increasing vs decreasing pushes.
# 7. Complexity: push / pop / top / getMin all O(1) time; O(n) space.
# 8. Follow-up if asked: "To cut space, use a second stack that only records
#    minimums, pushing on val <= current_min and popping on equality."
#
# Time:  O(1) per operation  (O(k) for k operations total)
# Space: O(n) for n elements in the stack
# =============================================================================


# =============================================================================
# SOLUTION 1: Pair stack — store (value, min_so_far)  (BEST)
# Remember as: "Every element carries its own min in its backpack."
# =============================================================================
class MinStackPairs:
    def __init__(self):
        self.stack = []  # list of (val, min_so_far)

    def push(self, val):
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]


# =============================================================================
# SOLUTION 2: Two stacks — data stack + min stack  (easy to remember)
# Remember as: "A second stack of record-lows; push on <=, pop when it matches."
# NOTE: the <= (not <) is the whole trick — it keeps duplicates of the minimum.
# =============================================================================
class MinStackTwoStacks:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        self.stack.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self):
        val = self.stack.pop()
        if self.mins and val == self.mins[-1]:
            self.mins.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.mins[-1]


# -----------------------------------------------------------------------------
# Harness: replays the operation list against a chosen implementation.
# -----------------------------------------------------------------------------
def min_stack_operations(operations, args, impl=MinStackPairs):
    results = []
    obj = None
    method_names = {"push": "push", "pop": "pop", "top": "top", "getMin": "get_min"}

    for op, arg in zip(operations, args):
        if op == "MinStack":
            obj = impl()
            results.append(None)
        else:
            results.append(getattr(obj, method_names[op])(*arg))
    return results


test_cases = [
    # (operations, args, expected)
    (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
     [[], [-2], [0], [-3], [], [], [], []],
     [None, None, None, None, -3, None, 0, -2]),

    (["MinStack", "push", "top", "getMin"],
     [[], [5], [], []],
     [None, None, 5, 5]),

    # duplicate minimum: popping one copy must keep min at 2
    (["MinStack", "push", "push", "pop", "getMin"],
     [[], [2], [2], [], []],
     [None, None, None, None, 2]),

    # strictly increasing pushes: min never changes
    (["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
     [[], [1], [2], [3], [], [], []],
     [None, None, None, None, 1, None, 1]),

    # strictly decreasing pushes: min must roll back as we pop
    (["MinStack", "push", "push", "push", "pop", "getMin", "pop", "getMin"],
     [[], [3], [2], [1], [], [], [], []],
     [None, None, None, None, None, 2, None, 3]),

    # negatives interleaved with queries
    (["MinStack", "push", "push", "getMin", "push", "getMin", "pop", "getMin", "top"],
     [[], [-1], [-2], [], [-3], [], [], [], []],
     [None, None, None, -2, None, -3, None, -2, -2]),

    # emptied then refilled: stale min must not survive
    (["MinStack", "push", "pop", "push", "getMin", "top"],
     [[], [4], [], [7], [], []],
     [None, None, None, None, 7, 7]),
]

for impl in (MinStackPairs, MinStackTwoStacks):
    print(f"--- {impl.__name__} ---")
    for i, (operations, args, expected) in enumerate(test_cases, 1):
        result = min_stack_operations(operations, args, impl)
        if result == expected:
            print(f"✅ Test {i} passed")
        else:
            print(f"❌ Test {i} FAILED: got {result}, expected {expected}")