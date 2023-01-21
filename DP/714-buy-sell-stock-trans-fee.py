# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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
        #         take = findMaxProfit(index + 1, prices, 1, dp) + prices[index] -fee
        #         notTake = findMaxProfit(index+1, prices, 0, dp)
        #         profit = max(take, notTake)

        #     dp[index][buy] = profit
        #     return dp[index][buy]
        
        # dp = [[-1] * 2 for _ in range(n)]
        # return findMaxProfit(0, prices, 1, dp)

        # Tabulation
        # dp = [[0] * 2 for _ in range(n+1)]

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
        #             take = dp[index + 1][1-buy] + prices[index] - fee
        #             notTake = dp[index+1][buy]
        #             profit = max(take, notTake)

        #         dp[index][buy] = profit

        # return dp[0][1]

        # Tabulation with space optimizaion
        ahead = [0] * 2

        ahead[0] = 0
        ahead[1] = 0

        for index in range(n-1, -1, -1):
            curr = [0] * 2
            for buy in range(2):
                profit = 0
                if buy:
                    take = ahead[1-buy] - prices[index]
                    notTake = ahead[buy]
                    profit = max(take, notTake)

                else:
                    take = ahead[1-buy] + prices[index] - fee
                    notTake = ahead[buy]
                    profit = max(take, notTake)

                curr[buy] = profit
            ahead = curr

        return ahead[1]