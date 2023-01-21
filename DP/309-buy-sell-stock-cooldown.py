# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Memoization
        # def findMaxProfit(index, prices, buy, dp):
        #     if index >= n:
        #         return 0

        #     if dp[index][buy] != -1:
        #         return dp[index][buy]

        #     profit = 0
        #     if buy:
        #         take = findMaxProfit(index + 1, prices, 0, dp) - prices[index]
        #         notTake = findMaxProfit(index+1, prices, 1, dp)
        #         profit = max(take, notTake)

        #     else:
        #         take = findMaxProfit(index + 2, prices, 1, dp) + prices[index]
        #         notTake = findMaxProfit(index+1, prices, 0, dp)
        #         profit = max(take, notTake)

        #     dp[index][buy] = profit
        #     return dp[index][buy]
        
        # dp = [[-1] * 2 for _ in range(n)]
        # return findMaxProfit(0, prices, 1, dp)

        # Tabulation
        # dp = [[0] * 2 for _ in range(n+2)]

        # dp[n][0] = 0
        # dp[n][1] = 0

        # for index in range(n-1, -1, -1):
        #     for buy in range(2):
        #         profit = 0
        #         if buy:
        #             take = dp[index + 1][1-buy] - prices[index]
        #             notTake = dp[index+1][buy]
        #             profit = max(take, notTake)

        #         else:
        #             take = dp[index + 2][1-buy] + prices[index]
        #             notTake = dp[index+1][buy]
        #             profit = max(take, notTake)

        #         dp[index][buy] = profit

        # return dp[0][1]

        # Tabulation with space optimizaion
        ahead1 = [0] * 2
        ahead2 = [0] * 2

        for index in range(n-1, -1, -1):
            curr = [0] * 2
            for buy in range(2):
                profit = 0
                if buy:
                    take = ahead1[1-buy] - prices[index]
                    notTake = ahead1[buy]
                    profit = max(take, notTake)

                else:
                    take = ahead2[1-buy] + prices[index]
                    notTake = ahead1[buy]
                    profit = max(take, notTake)

                curr[buy] = profit
            ahead2 = ahead1
            ahead1 = curr

        return ahead1[1]

