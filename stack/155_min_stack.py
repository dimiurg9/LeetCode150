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


def min_stack_operations(operations, args):
    pass


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

for i, (operations, args, expected) in enumerate(test_cases, 1):
    result = min_stack_operations(operations, args)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")