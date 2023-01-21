# We are given an array ‘ARR’ with N positive integers. We need to find if there is a subset in “ARR” with a sum equal to K. If there is, return true else return false.


from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
#     memoization
#     def findSubsetSum(index, target, arr, dp):
#         if target == 0:
#             return True
#         if index == 0:
#             return arr[index] == sum
#         if dp[index][target] != -1:
#             return dp[index][target]
        
#         toBe = False
#         if arr[index] <= target:
#             toBe = findSubsetSum(index-1, target - arr[index], arr, dp)
#         notToBe = findSubsetSum(index-1, target, arr, dp)
        
#         dp[index][target] = toBe or notToBe
#         return dp[index][target]

#     dp = [[-1] * (k+1)] * n
#     return findSubsetSum(n-1, k, arr, dp)

#     Tabulation
#     dp = [[0] * (k+1) for _ in range(n)]
    
#     for i in range(n):
#         dp[i][0] = True
        
#     if arr[0] <=k:
#         dp[0][arr[0]] = True
    
#     for index in range(1, n):
#         for target in range(1, k+1):
#             notToBe = dp[index-1][target]
#             toBe = False
#             if arr[index] <= target:
#                 toBe = dp[index-1][target - arr[index]]
            
#             dp[index][target] = toBe or notToBe
        
#     return dp[n-1][k]
            
#     Tabulation with space optimisation
    prev = [False] * (k+1)
    cur = [False] * (k+1)
    
    prev[0] = True
    cur[0] = True
    
    if arr[0] <=k:
        prev[arr[0]] = True
    
    for index in range(1, n):
        cur = [False] * (k+1)
        cur[0] = True
        for target in range(1, k+1):
            notToBe = prev[target]
            toBe = False
            if arr[index] <= target:
                toBe = prev[target - arr[index]]
            
            cur[target] = toBe or notToBe
            
        prev = cur
        
    return prev[k]

