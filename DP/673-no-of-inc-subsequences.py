# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        mx = 1

        for index in range(n):
            for prev in range(index):
                if nums[index] > nums[prev] and 1 + dp[prev] > dp[index]:
                    dp[index] = 1 + dp[prev]
                    count[index] = count[prev]
                elif nums[index] > nums[prev] and 1 + dp[prev] == dp[index]:
                    count[index] += count[prev]

            if dp[index] > mx:
                mx = dp[index]

        ans = 0
        for i in range(n):
            if dp[i] == mx:
                ans += count[i]

        return ans