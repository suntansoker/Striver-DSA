# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:

# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        MAX = 10 ** 9
        m = len(grid)
        n = len(grid[0])

        # Memoization
        # dp = [[-1] * n for _ in range(m)]
        # def findMinPath(i, j, grid, dp):
        #     if i==0 and j==0:
        #         dp[0][0] = grid[0][0]
        #         return dp[0][0]
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     if i<0 or j<0:
        #         return MAX

        #     else:
        #         top = MAX
        #         left = MAX

        #         if i>0:
        #             top = min(top, findMinPath(i-1, j, grid, dp))

        #         if j>0:
        #             left = min(left, findMinPath(i, j-1, grid, dp))

        #         dp[i][j] = grid[i][j] + min(left, top)

        #     return dp[i][j]
                
        # val = findMinPath(m-1, n-1, grid, dp)

        # return val

        # Tabulation
        # dp = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 and j==0:
        #             dp[0][0] = grid[0][0]
        #         else:
        #             top = MAX
        #             left = MAX

        #             if i>0:
        #                 top = min(top, dp[i-1][j])

        #             if j>0:
        #                 left = min(left, dp[i][j-1])

        #             dp[i][j] = grid[i][j] + min(left, top)

        # return dp[m-1][n-1]

        # Tabulation with space optimization
        prev = [0] * n
        for i in range(m):
            cur = [0] * n
            for j in range(n):
                if i==0 and j==0:
                    cur[j] = grid[0][0]
                else:
                    top = MAX
                    left = MAX

                    if i>0:
                        top = min(top, prev[j])

                    if j>0:
                        left = min(left, cur[j-1])

                    cur[j] = grid[i][j] + min(left, top)

            prev = cur

        return prev[n-1]

