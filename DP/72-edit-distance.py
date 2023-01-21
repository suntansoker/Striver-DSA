# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1] * n for _ in range(m)]

        def findMinDistance(word1, word2, index1, index2, dp):
            if index1<0:
                return index2 + 1
            if index2 < 0:
                return index1 + 1

            if dp[index1][index2] != -1:
                return dp[index1][index2]

            if word1[index1] == word2[index2]:
                dp[index1][index2] = findMinDistance(word1, word2, index1-1, index2-1, dp)
            else:
                insert = 1 + findMinDistance(word1, word2, index1, index2-1, dp)
                delete = 1 + findMinDistance(word1, word2, index1-1, index2, dp)
                replace = 1 + findMinDistance(word1, word2, index1-1, index2-1, dp)
                dp[index1][index2] = min(insert, delete, replace)

            return dp[index1][index2]
        return findMinDistance(word1, word2 , m-1, n-1, dp)