"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
                 profit = 6-1 = 5.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: No transactions are done, max profit = 0.

Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4
"""

from typing import List

# ============================================================
# INTERVIEW PLAN
# ============================================================
# 1. "This is a one-pass problem. I need to find the max difference
#     prices[j] - prices[i] where j > i."
# 2. "I'll track the minimum price seen so far as I scan left to right."
# 3. "At each day, the best profit if I sell TODAY is today's price minus
#     the cheapest price I've seen before today."
# 4. "I keep a running max of that profit."
# 5. "Edge cases: single element → 0, all decreasing → 0, all equal → 0."
#
# Time:  O(n) — single pass
# Space: O(1) — two variables
# ============================================================


# ------------------------------------------------------------------
# SOLUTION 1: Track Min Price (BEST)
# ------------------------------------------------------------------
# Remember as: "Track the cheapest day so far; at each day compute profit if selling today."

def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    best_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        best_profit = max(best_profit, price - min_price)

    return best_profit


# ------------------------------------------------------------------
# SOLUTION 2: Kadane's Variant on Daily Gains (easy to remember)
# ------------------------------------------------------------------
# Remember as: "Convert to daily changes, then find max subarray sum (can't go negative)."

def max_profit_kadane(prices: List[int]) -> int:
    current_gain = 0
    max_gain = 0

    for i in range(1, len(prices)):
        daily_change = prices[i] - prices[i - 1]
        current_gain = max(0, current_gain + daily_change)
        max_gain = max(max_gain, current_gain)

    return max_gain


# ============================================================
# TEST CASES
# ============================================================
test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2], 1),
    ([2, 4, 1], 2),
    ([2, 1, 2, 1, 0, 1, 2], 2),
    ([1], 0),
    ([3, 3, 3, 3], 0),
    ([2, 1, 4], 3),
]

print("--- Solution 1: Track Min Price ---")
for i, (prices, expected) in enumerate(test_cases, 1):
    result = max_profit(prices)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")

print("\n--- Solution 2: Kadane's Variant ---")
for i, (prices, expected) in enumerate(test_cases, 1):
    result = max_profit_kadane(prices)
    if result == expected:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} FAILED: got {result}, expected {expected}")