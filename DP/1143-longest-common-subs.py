'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # Memoization
        dp = [[-1] * n for _ in range(m)]
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
                
        return findLCS(text1, text2, m-1, n-1, dp)
        # Tabulation
        # dp = [[0] * (n+1) for _ in range(m+1)]

        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # i = m
        # j = n
        # lcsString = ""
        # while(i>0 and j>0):
        #     if text1[i-1] == text2[j-1]:
        #         lcsString = text1[i-1] + lcsString
        #         i -= 1
        #         j -= 1
        #     else:
        #         if dp[i-1][j] > dp[i][j-1]:
        #             i -= 1
        #         else:
        #             j -= 1
        # print(lcsString)


        # return dp[m][n]



