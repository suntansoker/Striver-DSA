# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:

# Input: m = 3, n = 7
# Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        
        # Memoization
        
        # dp[0][0] = 1
        # def findPaths(i, j, dp):
        #     if i==0 and j==0:
        #         return dp[0][0]

        #     if dp[i][j] != -1:
        #         return dp[i][j]

            # left = 0
            # top = 0
            # if i-1>=0:
            #     left = findPaths(i-1, j,dp)
            # if j-1>=0:
            #     top = findPaths(i, j-1, dp)

            # dp[i][j] = top + left
        #     return dp[i][j]

        # val = findPaths(m-1, n-1, dp)
        # return val

        # return dp[m-1][n-1]

        #Tabulation

        # for i in range(m):
        #     for j in range(n):
        #         if i==0 and j==0:
        #             dp[0][0] = 1
                
        #         else:
        #             left = 0
        #             top = 0
        #             if i-1>=0:
        #                 left = dp[i-1][j]
        #             if j-1>=0:
        #                 top = dp[i][j-1]

        #             dp[i][j] = top + left

        # return dp[m-1][n-1]

        #Tabulation with O(n) space

        prev = [0] * n

        for i in range(m):
            cur = [0] * n
            for j in range(n):
                if i==0 and j==0:
                    cur[j] = 1
                else:
                    left = 0
                    top = 0
                    if j-1>=0:
                        left = cur[j-1]
                    if i-1>=0:
                        top = prev[j]

                    cur[j] = top + left

            prev = cur

        return prev[n-1]

            


                
