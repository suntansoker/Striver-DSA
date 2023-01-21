# You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.

# Example 1:

# Input:
# N = 3
# W = 4
# values[] = {1,2,3}
# weight[] = {4,5,1}
# Output: 3

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # Memoization
        # dp = [[-1] * (W+1) for _ in range(n)]
        # def findKnapsack(index, W, wt, val, dp):
        #     if index==0:
        #         if wt[index]<=W:
        #             return val[index]
        #         else:
        #             return 0
                    
        #     if dp[index][W] != -1:
        #         return dp[index][W]
                
        #     take = -(10 ** 9)
        #     if wt[index]<=W:
        #         take = val[index]+findKnapsack(index-1, W- wt[index], wt, val, dp)
        #     notTake = findKnapsack(index-1, W, wt, val, dp)
        #     dp[index][W] = max(take, notTake)
            
        #     return dp[index][W]
        # return findKnapsack(n-1,W, wt, val, dp)
        
        # Tabulation
        # dp = [[0] * (W+1) for _ in range(n)]
        
        # for i in range(wt[0], W+1):
        #     dp[0][i] = val[0]
            
        # for index in range(1, n):
        #     for weight in range(0, W+1):
        #         take = -(10 ** 9)
        #         if wt[index]<=weight:
        #             take = val[index]+dp[index-1][weight- wt[index]]
        #         notTake = dp[index-1][weight]
        #         dp[index][weight] = max(take, notTake)
                
        # return dp[n-1][W]
        
        # Tabulation with space optimization
        prev= [0] * (W+1)
        
        for i in range(wt[0], W+1):
            prev[i] = val[0]
            
        for index in range(1, n):
            cur = [0] * (W+1)
            for weight in range(0, W+1):
                take = -(10 ** 9)
                if wt[index]<=weight:
                    take = val[index]+prev[weight- wt[index]]
                notTake = prev[weight]
                cur[weight] = max(take, notTake)
                
            prev = cur
                
        return prev[W]