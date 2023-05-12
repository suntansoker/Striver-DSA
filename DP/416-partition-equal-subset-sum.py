# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumA = 0
        n = len(nums)
        for i in range(n):
            sumA += nums[i]

        if sumA%2 != 0:
            return False

        k = sumA//2

        prev = [False] * (k+1)
        prev[0] = True

        if nums[0]<=k:
            prev[nums[0]] = True

        for index in range(1, n):
            cur = [False] * (k+1)
            cur[0] = True
            for target in range(1, k+1):
                taken = False
                if nums[index]<=target:
                    taken = prev[target-nums[index]]
                notTaken = prev[target]
                cur[target] = taken or notTaken

            prev = cur

        return prev[k]

