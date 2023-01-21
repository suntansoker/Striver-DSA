# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        # dp = [[[0 for i in range(3)] for j in range(2)] for _ in range(n+1)]

        # for index in range(n-1, -1, -1):
        #     for buy in range(2):
        #         for cap in range(1, 3):
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

        # return dp[0][1][2]

        # Tabulation with space optimizaion
        ahead = [[0 for i in range(3)] for j in range(2)]

        for index in range(n-1, -1, -1):
            curr = [[0 for i in range(3)] for j in range(2)]
            for buy in range(2):
                for cap in range(1, 3):
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

        return ahead[1][2]
