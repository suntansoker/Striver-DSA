# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

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
        #             take = dp[index + 1][1-buy] + prices[index]
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
                    take = ahead[1-buy] + prices[index]
                    notTake = ahead[buy]
                    profit = max(take, notTake)

                curr[buy] = profit
            ahead = curr

        return ahead[1]

