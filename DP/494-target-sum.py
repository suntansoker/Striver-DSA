# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def findNumber(nums, index, target, dp):
            if index == 0:
                if target==0 and nums[index] == 0:
                    return 2
                if nums[index] == target or target == 0:
                    return 1
                return 0


            if dp[index][target] != -1:
                return dp[index][target]

            take = 0
            if nums[index]<=target:
                take = findNumber(nums, index-1, target-nums[index], dp)
            notTake = findNumber(nums, index-1, target, dp)

            dp[index][target] = take + notTake
            return dp[index][target]

        tar = 0
        for i in range(len(nums)):
            tar += nums[i]

        if tar - target < 0 or (tar - target) % 2 != 0:
            return 0
        n = len(nums)
        newTar = (tar-target) // 2
        dp = [[-1 for i in range(newTar+1)] for _ in range(n)]
        return findNumber(nums, n-1, (tar-target) // 2, dp)