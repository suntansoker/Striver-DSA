# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s2 = "".join(reversed(s))
        dp = [[-1] * n for _ in range(n)]
        def findLCS(text1, text2, index1, index2, dp):
            if index1 < 0 or index2 < 0:
                return 0
            if dp[index1][index2] != -1:
                return dp[index1][index2]
            if text1[index1] == text2[index2]:
                dp[index1][index2] = 1 + findLCS(text1, text2, index1-1, index2-1, dp)
            else:
                remove1 = findLCS(text1, text2, index1-1, index2, dp)
                remove2 = findLCS(text1, text2, index1, index2-1, dp)
                dp[index1][index2] = max(remove1, remove2)

            return dp[index1][index2]
                
        f = findLCS(s, s2, n-1, n-1, dp)
        return n - f