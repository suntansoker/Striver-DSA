from os import *
from sys import *
from collections import *
from math import *

def evaluateExp(exp):
    n = len(exp)
    dp = [[[-1 for _ in range(2)] for i in range(n)] for j in range(n)]
    MOD = 1000000007
    def findNumberOfWays(i, j, isTrue, exp, dp):
        if i>j:
            return 0
        if i==j:
            if(isTrue):
                return exp[i] == 'T'
            else:
                return exp[i] == 'F'
            
        if dp[i][j][isTrue] != -1:
            return dp[i][j][isTrue]
        ways = 0
        for p in range(i+1, j, 2):
            lf = findNumberOfWays(i, p-1, 0, exp, dp)
            lt = findNumberOfWays(i, p-1, 1, exp, dp)
            rf = findNumberOfWays(p+1, j, 0, exp, dp)
            rt = findNumberOfWays(p+1, j, 1, exp, dp)
            
            if exp[p] == '|':
                if isTrue == 1:
                    ways = (ways +(lf * rt) % MOD + (lt * rt) % MOD + (lt * rf) % MOD) % MOD
                else:
                    ways = ways + (lf * rf) % MOD
                    
            elif exp[p] == '&':
                if isTrue == 1:
                    ways = ways + (lt * rt) % MOD
                else:
                    ways = (ways + (lf * rf) % MOD + (lt * rf) % MOD + (lf * rt) % MOD) % MOD
                    
            else:
                if isTrue == 1:
                    ways = (ways +(lf * rt) % MOD + (lt * rf) % MOD) % MOD
                else:
                    ways = (ways +(lf * rf) % MOD + (lt * rt) % MOD) % MOD
                    
        dp[i][j][isTrue] = ways
        return dp[i][j][isTrue]
                
            
    return findNumberOfWays(0, n-1, 1, exp, dp) % MOD