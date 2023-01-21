'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        heapq.heapify(arr)

        for i in range(len(nums)):
            heapq.heappush(arr, -nums[i])

        while k>0:
            popped = -1 * heapq.heappop(arr)
            k -= 1

        return popped