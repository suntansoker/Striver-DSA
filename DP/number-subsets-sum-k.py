# Given an array arr[] of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

# Note: Answer can be very large, so, output answer modulo 109+7

# Example 1:

# Input: N = 6, arr[] = {2, 3, 5, 6, 8, 10}
#        sum = 10
# Output: 3
# Explanation: {2, 3, 5}, {2, 8}, {10}

# NOT WORKING

class Solution:
	def perfectSum(self, arr, n, k):
    prev = [0] * (k+1)
    cur = [0] * (k+1)
    prev[0] = 1
    cur[0] = 1
    if arr[0] <=k:
        prev[arr[0]] = 1
    for index in range(1, n):
          cur = [0] * (k+1)
          cur[0] = 1
          for target in range(1, k+1):
              notToBe = prev[target]
              toBe = 0
              if arr[index] <= target:
                  toBe = prev[target - arr[index]]
                  
              cur[target] = toBe + notToBe
          prev = cur
          
    return prev[k]