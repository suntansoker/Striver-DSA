# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def findNumberofCoins(coins, index, maxAmount, dp):
            if index == 0:
                if maxAmount % coins[index] == 0:
                    return 1
                else:
                    return 0

            if dp[index][maxAmount] != -1:
                return dp[index][maxAmount]

            take = 0
            if coins[index] <= maxAmount:
                take = findNumberofCoins(coins, index, maxAmount- coins[index], dp)
            notTake = findNumberofCoins(coins, index-1, maxAmount, dp)

            dp[index][maxAmount] = take + notTake
            return dp[index][maxAmount]
        
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        return findNumberofCoins(coins, n-1, amount, dp)