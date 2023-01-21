'''
Given an array of positive integers. Find the maximum length of Bitonic subsequence. 
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing.
 

Example 1:

Input: nums = [1, 2, 5, 3, 2]
Output: 5
Explanation: The sequence {1, 2, 5} is
increasing and the sequence {3, 2} is 
decreasing so merging both we will get 
length 5.
Example 2:

Input: nums = [1, 11, 2, 10, 4, 5, 2, 1]
Output: 6
Explanation: The bitonic sequence 
{1, 2, 10, 4, 2, 1} has length 6
'''

class Solution:
	def LongestBitonicSequence(self, nums):
        n = len(nums)
        dp1 = [1] * n
        
        mx = 0
        for index in range(n):
            for prev in range(index):
                if nums[index] > nums[prev] and 1 + dp1[prev] > dp1[index]:
                    dp1[index] = 1 + dp1[prev]
                    
        dp2 = [1] * n

        for index in range(n-1, -1, -1):
            for prev in range(n-1, index, -1):
                if nums[index] > nums[prev] and 1 + dp2[prev] > dp2[index]:
                    dp2[index] = 1 + dp2[prev]
                    
        for i in range(n):
            mx = max(mx, dp1[i] + dp2[i] - 1)
            
        return mx