'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
'''

class Solution:
    def minCut(self, s: str) -> int:
        # MEMOIZATION
        # n = len(s)
        # dp = [-1] * n
        # pMatrix = [[False] * n for _ in range(n)]

        # def isPalindrome(s, i1, j1):
        #     while i1<j1:
        #         if s[i1] != s[j1]:
        #             return False
        #         i1 += 1
        #         j1 -= 1
        #     return True
            
        # def findMinCuts(i, n, s, dp):
        #     if i==n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     st = ""
        #     minCut = 10 ** 9
        #     for j in range(i, n):
        #         if pMatrix[i][j]:
        #             cuts = 1 + findMinCuts(j+1, n, s, dp)
        #             if cuts < minCut:
        #                 minCut = cuts
        #     dp[i] = minCut
        #     return dp[i]

        # for a in range(n):
        #     for b in range(a,n):
        #         pMatrix[a][b] = isPalindrome(s, a, b)

        # return findMinCuts(0, n, s, dp) - 1

        # TABULATION
        n = len(s)
        pMatrix = [[False] * n for _ in range(n)]

        def isPalindrome(s, i1, j1):
            while i1<j1:
                if s[i1] != s[j1]:
                    return False
                i1 += 1
                j1 -= 1
            return True

        for a in range(n):
            for b in range(a,n):
                pMatrix[a][b] = isPalindrome(s, a, b)

        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            minCut = 10 ** 9
            for j in range(i, n):
                if pMatrix[i][j]:
                    cuts = 1 + dp[j+1]
                    if cuts < minCut:
                        minCut = cuts
            dp[i] = minCut

        return dp[0] - 1

