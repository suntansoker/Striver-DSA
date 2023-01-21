'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[-1] * n for _ in range(m)]
        def findWildcardMatch(s, p, indexS, indexP, dp):
            if indexS < 0 and indexP < 0:
                return True
            if indexP < 0 and indexS >= 0:
                return False
            if indexS < 0 and indexP >= 0:
                for j in range(indexP, -1, -1):
                    if p[j] != "*":
                        return False
                return True

            if dp[indexS][indexP] != -1:
                return dp[indexS][indexP]

            if s[indexS] == p[indexP] or p[indexP] == "?":
                dp[indexS][indexP] = findWildcardMatch(s, p, indexS-1, indexP-1, dp)
            else:
                if p[indexP] == "*":
                    dp[indexS][indexP] = findWildcardMatch(s, p, indexS, indexP-1, dp) or findWildcardMatch(s, p, indexS-1, indexP, dp)
                else:
                    dp[indexS][indexP] = False

            return dp[indexS][indexP]
            
        return findWildcardMatch(s, p, m-1, n-1, dp)