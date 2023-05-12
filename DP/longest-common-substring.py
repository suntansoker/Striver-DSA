# Given two strings. The task is to find the length of the longest common substring.

# Example 1:

# Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
# Output: 4
# Explanation: The longest common substring
# is "CDGH" which has length 4.

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0] * (m+1) for _ in range(n+1)]
        mx = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    mx = max(mx, dp[i][j])
                else:
                    dp[i][j] = 0
                    
        return mx