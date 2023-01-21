# We are given an array ‘ARR’ with N positive integers. We need to partition the array into two subsets such that the absolute difference of the sum of elements of the subsets is minimum.

# We need to return only the minimum absolute difference of the sum of elements of the two partitions

def minSubsetSumDifference(arr, n):
    k = 0
    for i in range(len(arr)):
        k += arr[i]
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
        
    mn = 10 ** 9
    for i in range(0, k+1):
        if prev[i] == True:
            firstSum = i
            secondSum = k-i
            mn = min(mn, abs(firstSum - secondSum))
            
    return mn