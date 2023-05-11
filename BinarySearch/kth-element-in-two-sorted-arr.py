# Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element that would be at the k’th position of the final sorted array.
 

# Example 1:

# Input:
# arr1[] = {2, 3, 6, 7, 9}
# arr2[] = {1, 4, 8, 10}
# k = 5
# Output:
# 6
# Explanation:
# The final sorted array would be -
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.
# Example 2:
# Input:
# arr1[] = {100, 112, 256, 349, 770}
# arr2[] = {72, 86, 113, 119, 265, 445, 892}
# k = 7
# Output:
# 256
# Explanation:
# Final sorted array is - 72, 86, 100, 112,
# 113, 119, 256, 265, 349, 445, 770, 892
# 7th element of this array is 256.

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if len(arr2) < len(arr1):
            return self.kthElement(arr2, arr1, m, n, k)
        high = k if k<n else n
        low = 0 if m>=k else k-m
        
        MIN = - 10 ** 9
        MAX = 10 ** 9
        while(low <= high):
            cut1 = (low + high) // 2
            cut2 = k - cut1
            
            if cut1 == 0:
                l1 = MIN
            else:
                l1 = arr1[cut1-1]
                
            if cut2 == 0:
                l2 = MIN
            else:
                l2 = arr2[cut2-1]
                
            if cut1 == n:
                r1 = MAX
            else:
                r1 = arr1[cut1]
                
            if cut2 == m:
                r2 = MAX
            else:
                r2 = arr2[cut2]
                
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1>r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
                
        return -1