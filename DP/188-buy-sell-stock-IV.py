# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # Memoization
        # def findMaxProfit(index, prices, buy, dp):
        #     if index == n:
        #         return 0

        #     if dp[index][buy] != -1:
        #         return dp[index][buy]

        #     profit = 0
        #     if buy:
        #         take = findMaxProfit(index + 1, prices, 0, dp) - prices[index]
        #         notTake = findMaxProfit(index+1, prices, 1, dp)
        #         profit = max(take, notTake)

        #     else:
        #         take = findMaxProfit(index + 1, prices, 1, dp) + prices[index]
        #         notTake = findMaxProfit(index+1, prices, 0, dp)
        #         profit = max(take, notTake)

        #     dp[index][buy] = profit
        #     return dp[index][buy]
        
        # dp = [[-1] * 2 for _ in range(n)]
        # return findMaxProfit(0, prices, 1, dp)

        # Tabulation
        # dp = [[[0 for i in range(k+1)] for j in range(2)] for _ in range(n+1)]

        # for index in range(n-1, -1, -1):
        #     for buy in range(2):
        #         for cap in range(1, k+1):
        #             profit = 0
        #             if buy:
        #                 take = dp[index + 1][0][cap] - prices[index]
        #                 notTake = dp[index+1][1][cap]
        #                 profit = max(take, notTake)
        #             else:
        #                 take = dp[index + 1][1][cap-1] + prices[index]
        #                 notTake = dp[index+1][0][cap]
        #                 profit = max(take, notTake)

        #             dp[index][buy][cap] = profit

        # return dp[0][1][k]

        # Tabulation with space optimizaion
        ahead = [[0 for i in range(k+1)] for j in range(2)]

        for index in range(n-1, -1, -1):
            curr = [[0 for i in range(k+1)] for j in range(2)]
            for buy in range(2):
                for cap in range(1, k+1):
                    profit = 0
                    if buy:
                        take = ahead[1-buy][cap] - prices[index]
                        notTake = ahead[buy][cap]
                        profit = max(take, notTake)

                    else:
                        take = ahead[1-buy][cap-1] + prices[index]
                        notTake = ahead[buy][cap]
                        profit = max(take, notTake)

                    curr[buy][cap] = profit

            ahead = curr

        return ahead[1][k]