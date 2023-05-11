# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # Memoization
        # dp = [[-1] * (amount+1) for _ in range(n)]
        # def findCoinChange(index, maxAmount, coins):
        #     if index == 0:
        #         if maxAmount % coins[index] == 0:
        #             return maxAmount // coins[index]
        #         else:
        #             return 10 ** 9
        #     if dp[index][maxAmount] != -1:
        #         return dp[index][maxAmount]
            
        #     taken = 10 ** 9
        #     if coins[index] <= maxAmount:
        #         taken = 1 + findCoinChange(index, maxAmount - coins[index], coins)
        #     notTaken = findCoinChange(index - 1, maxAmount, coins)

        #     dp[index][maxAmount] = min(taken, notTaken)
        #     return dp[index][maxAmount]

        # val = findCoinChange(n-1, amount, coins)
        # if val >= (10 ** 9):
        #     return -1

        # return val

        # Tabulation
        # dp = [[0] * (amount + 1) for _ in range(n)]
        # for amt in range(0, amount+1):
        #     if amt % coins[0] == 0:
        #         dp[0][amt] = amt // coins[0]
        #     else:
        #         dp[0][amt] = 10 ** 9

        # for index in range(1, n):
        #     for maxAmount in range(0, amount + 1):
        #         taken = 10 ** 9
        #         if coins[index] <= maxAmount:
        #             taken = 1 + dp[index][maxAmount - coins[index]]
        #         notTaken = dp[index - 1][maxAmount]

        #         dp[index][maxAmount] = min(taken, notTaken)

        # if dp[n-1][amount]>= 10 ** 9:
        #     return -1
        # else:
        #     return dp[n-1][amount]

        # Tabulation with space optimization
        prev = [0] * (amount + 1)
        for amt in range(0, amount+1):
            if amt % coins[0] == 0:
                prev[amt] = amt // coins[0]
            else:
                prev[amt] = 10 ** 9

        for index in range(1, n):
            curr = [0] * (amount + 1)
            for maxAmount in range(0, amount + 1):
                taken = 10 ** 9
                if coins[index] <= maxAmount:
                    taken = 1 + curr[maxAmount - coins[index]]
                notTaken = prev[maxAmount]

                curr[maxAmount] = min(taken, notTaken)

            prev = curr

        if prev[amount]>= 10 ** 9:
            return -1
        else:
            return prev[amount]