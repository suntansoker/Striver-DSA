'''
You are given N number of books. Every ith book has Ai number of pages. 
You have to allocate contiguous books to M number of students. There can be many ways or permutations to do so. In each permutation, one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is the minimum of those in all the other permutations and print this minimum value.

Each book will be allocated to exactly one student. Each student has to be allocated at least one book.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

Example 1:

Input:
N = 4
A[] = {12,34,67,90}
M = 2
Output:113
Explanation:Allocation can be done in 
following ways:{12} and {34, 67, 90} 
Maximum Pages = 191{12, 34} and {67, 90} 
Maximum Pages = 157{12, 34, 67} and {90} 
Maximum Pages =113. Therefore, the minimum 
of these cases is 113, which is selected 
as the output.

Example 2:

Input:
N = 3
A[] = {15,17,20}
M = 2
Output:32
Explanation: Allocation is done as
{15,17} and {20}
'''

class Solution: 
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        low,high = A[0], A[0]
        for i in range(1, N):
            low = min(low, A[i])
            high += A[i]
            
        res = -1
        
        def goodAllocation(A, barrier, M):
            total, no = 0, 1
            for i in range(N):
                if A[i] > barrier:
                    return False
                if total + A[i] > barrier:
                    no += 1
                    total = A[i]
                else:
                    total += A[i]
                    
            if no > M:
                return False
            else:
                return True
                
        if M > N:
            return res
                
        while(low<=high):
            mid = (low + high) // 2
            if goodAllocation(A, mid, M):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res