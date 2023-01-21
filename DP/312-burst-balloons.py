'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        # MEMOIZATION
        # dp = [[-1] * (n+1) for _ in range(n+1)]
        # def findMaxCoins(i, j, nums, dp):
        #     if i>j:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     maxi = -1
        #     for k in range(i, j+1):
        #         points = nums[i-1] * nums[k] * nums[j+1] + findMaxCoins(i, k-1, nums, dp) + findMaxCoins(k+1, j, nums, dp)
        #         maxi = max(maxi, points)

        #     dp[i][j] = maxi
        #     return dp[i][j]

        # return findMaxCoins(1, n, nums, dp)

        # TABULATION
        dp = [[0] * (n+2) for _ in range(n+2)]
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                maxi = -1
                for k in range(i, j+1):
                    points = nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    maxi = max(maxi, points)

                dp[i][j] = maxi

        return dp[1][n]

