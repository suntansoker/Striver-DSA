# Given two strings s and t, return the number of distinct 
# subsequences
#  of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        # Memoization
        # dp = [[-1] * (nt) for _ in range(ns)]
        # def findDistinct(s, t, indexS, indexT, dp):
        #     if indexT < 0:
        #         return 1
        #     if indexS < 0:
        #         return 0
        #     if dp[indexS][indexT] != -1:
        #         return dp[indexS][indexT]
        #     take = 0
        #     if s[indexS] == t[indexT]:
        #         take = findDistinct(s, t, indexS-1, indexT-1, dp)
        #     notTake = findDistinct(s, t, indexS-1, indexT, dp)
        #     dp[indexS][indexT] = take + notTake

        #     return dp[indexS][indexT]
            
        # return findDistinct(s, t, ns-1, nt-1, dp)

        # Tabulation
        dp = [[0] * (nt+1) for _ in range(ns+1)]
        for i in range(ns+1):
            dp[i][0] = 1

        for i in range(1, ns+1):
            for j in range(1, nt+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[ns][nt]


