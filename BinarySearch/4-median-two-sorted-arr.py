# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            val = self.findMedianSortedArrays(nums2, nums1)
            return val
        n1 = len(nums1)
        n2 = len(nums2)
        MIN = - 10 ** 9
        MAX = 10 ** 9

        low, high = 0, n1
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1
            if cut1 == 0:
                l1 = MIN
            else:
                l1 = nums1[cut1 - 1]

            if cut2 == 0:
                l2 = MIN
            else:
                l2 = nums2[cut2 - 1]

            if cut1 == n1:
                r1 = MAX
            else:
                r1 = nums1[cut1]

            if cut2 == n2:
                r2 = MAX
            else:
                r2 = nums2[cut2]

            if l1<=r2 and l2<=r1:
                if (n1+n2)%2 ==0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1>r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return 0.0