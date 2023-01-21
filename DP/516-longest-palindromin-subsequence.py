# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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
                
        return findLCS(s, s2, n-1, n-1, dp)