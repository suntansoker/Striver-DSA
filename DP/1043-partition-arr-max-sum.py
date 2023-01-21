'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
'''

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # MEMOIZATION
        # n = len(arr)
        # dp = [-1] * n
        # def findmaxSumAfterPartitioning(i, n, arr, dp):
        #     if i == n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     length, maxi = 0, -1
        #     smMax = (-10) ** 9
        #     for j in range(i, min(n, i+k)):
        #         length += 1
        #         maxi = max(arr[j], maxi)
        #         sm = maxi * length + findmaxSumAfterPartitioning(j+1, n, arr, dp)
        #         smMax = max(smMax, sm)
        #     dp[i] = smMax
        #     return dp[i]

        # return findmaxSumAfterPartitioning(0, n, arr, dp)

        # TABULATION
        n = len(arr)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            length, maxi = 0, -1
            smMax = (-10) ** 9
            for j in range(i, min(n, i+k)):
                length += 1
                maxi = max(arr[j], maxi)
                sm = maxi * length + dp[j+1]
                smMax = max(smMax, sm)
            dp[i] = smMax

        return dp[0]