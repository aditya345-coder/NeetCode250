# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""Problem Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


# Brute Force Solution: Time Complexity: O(n^2); Space Time Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmax=0; maximum=0
        for l in range(len(prices)):
            for r in range(l+1,len(prices)):
                val=prices[r]-prices[l]
                if (val>cmax):
                    cmax=val
                if (prices[l]>prices[r]):
                    break
            maximum=max(cmax, maximum)
        return maximum

# Brute Force Solution: Time Complexity: O(n); Space Time Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0]; maximum=0
        for i in range(1,len(prices)):
            curr_profit=prices[i]-buy_price
            if (curr_profit>maximum):
                maximum=curr_profit
            if (prices[i]<buy_price):
                buy_price=prices[i]
        return maximum
