def findNthRoot(x, n):
    low = 1
    high = x
    epsilon = 10 ** (-6)

    def multiply(no, n):
        ans = 1
        for i in range(1, n+1):
            ans *= no

        return ans

    while(high - low > epsilon):
        mid = (high + low) / 2
        if multiply(mid, n) < x:
            low = mid
        else:
            high = mid

    return low

        