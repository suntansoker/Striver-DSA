'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        hash = [0] * n
        mx = 1
        lastIndex = 0
        for index in range(n):
            hash[index] = index
            for prev in range(index):
                if nums[index] % nums[prev] == 0 and 1 + dp[prev] > dp[index]:
                    dp[index] = 1 + dp[prev]
                    hash[index] = prev

            if dp[index] > mx:
                mx = dp[index]
                lastIndex = index

        res = []
        res.append(nums[lastIndex])
        while(hash[lastIndex] != lastIndex):
            lastIndex = hash[lastIndex]
            res.append(nums[lastIndex])

        res.reverse()
        
        return res

