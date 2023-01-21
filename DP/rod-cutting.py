# Given a rod of length N inches and an array of prices, price[]. pricei denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

# Example 1:

# Input:
# N = 8
# Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
# Output:
# 22
# Explanation:
# The maximum obtainable value is 22 by
# cutting in two pieces of lengths 2 and 
# 6, i.e., 5+17=22.

class Solution:
    def cutRod(self, price, n):
        def findMax(price, index, maxSize, dp):
            if index == 0:
                return maxSize * price[index]
                
            if dp[index][maxSize] != -1:
                return dp[index][maxSize]
                
            take = 0
            if index+1 <= maxSize:
                take = price[index] + findMax(price, index, maxSize - index - 1, dp)
            notTake = findMax(price, index-1, maxSize, dp)
            
            dp[index][maxSize] = max(take, notTake)
            return dp[index][maxSize]
                    
        l = len(price)
        dp = [[-1] * (n+1) for _ in range(l)]
        return findMax(price, l-1, n, dp)