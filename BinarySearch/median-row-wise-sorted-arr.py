# Given a row wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.

# Example 1:

# Input:
# R = 3, C = 3
# M = [[1, 3, 5], 
#      [2, 6, 9], 
#      [3, 6, 9]]
# Output: 5
# Explanation: Sorting matrix elements gives 
# us {1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 
 

# Example 2:

# Input:
# R = 3, C = 1
# M = [[1], [2], [3]]
# Output: 2
# Explanation: Sorting matrix elements gives 
# us {1,2,3}. Hence, 2 is median.

class Solution:
    def median(self, matrix, R, C):
    	low = 1
    	high = 2000
    	
    	def findElementsLessOrEqual(mid, k, row):
    	    count = 0
	        l, h = 0, len(row)-1
	        while(l <= h):
	            m = (l + h) // 2
	            if row[m] <= mid:
	                l = m + 1
	            else:
	                h = m - 1
	                
	        return l
	           
    	
    	k = (R * C) // 2
    	while low <= high:
    	    count = 0
    	    mid = (low + high) // 2
    	    for i in range(len(matrix)):
    	        no = findElementsLessOrEqual(mid, k, matrix[i])
    	        count += no
    	    if count <= k:
    	        low = mid + 1
    	    else:
    	        high = mid - 1
    	        
        # return low