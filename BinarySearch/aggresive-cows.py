class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        low, high = 1, stalls[n-1]-stalls[0]
        ans = 0
        def goodSplit(stalls, mid, k, n):
            count = 1
            idx = 0
            for i in range(1, n):
                if stalls[i] - stalls[idx] >= mid:
                    idx = i
                    count += 1
            if count >= k:
                return True
            else:
                return False
            
        while low <= high:
            mid = (low + high) // 2
            if goodSplit(stalls, mid, k, n):
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
                
        return ans