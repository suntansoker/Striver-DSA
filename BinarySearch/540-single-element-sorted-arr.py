# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 2
        while(low <= high):
            mid = (low + high) // 2
            if mid % 2 == 0:
                if (mid + 1) < len(nums) and mid >=0 and nums[mid + 1] == nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid-1) >= 0 and mid < len(nums) and nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1

        return nums[low]