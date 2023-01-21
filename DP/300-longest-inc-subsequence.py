'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # MEMOIZATION
        # n = len(nums)
        # dp = [[-1] * (n+1) for _ in range(n)]
        # def findLIS(index, prev, nums, dp):
        #     if index >= n:
        #         return 0
        #     if dp[index][prev+1] != -1:
        #         return dp[index][prev+1]

        #     notTake = findLIS(index+1, prev, nums, dp)

        #     take = 0
        #     if prev == -1 or nums[index] > nums[prev]:
        #         take = 1 + findLIS(index+1, index, nums, dp)

        #     dp[index][prev + 1] = max(take, notTake)

        #     return dp[index][prev+1]

        # return findLIS(0, -1, nums, dp)

        # TABULATION
        # n = len(nums)
        # dp = [1] * n
        # mx = 1
        # lastIndex = 0
        # for index in range(n):
        #     for prev in range(index):
        #         if nums[index] > nums[prev] == 0 and 1 + dp[prev] > dp[index]:
        #             dp[index] = 1 + dp[prev]

        #     if dp[index] > mx:
        #         mx = dp[index]
        #         lastIndex = index

        # return mx

        #TABULATION WITH BIN SEARCH (nlogn)
        temp = []
        temp.append(nums[0])
        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                idx = bisect.bisect_left(temp, nums[i])
                temp[idx] = nums[i]

        return len(temp)