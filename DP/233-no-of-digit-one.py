# DIGIT DP

# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# Example 1:

# Input: n = 13
# Output: 6
# Example 2:

# Input: n = 0
# Output: 0


# Constraints:

# 0 <= n <= 10^9

class Solution:
    def countDigitOne(self, n: int) -> int:
        num = str(n)
        lenNum = len(num)
        dp = {}

        def findNumbers(index, tight, total):
            if index >= len(str(n)):
                return total

            if (index, tight, total) in dp:
                return dp[(index, tight, total)]
            high = 0
            if tight == 1:
                high = int(num[index])
            else:
                high = 9

            count = 0
            for i in range(high+1):
                a = total
                if i == 1:
                    a += 1
                if i < int(num[index]):
                    count += findNumbers(index+1, 0, a)
                else:
                    count += findNumbers(index+1, tight, a)

            dp[(index, tight, total)] = count
            return dp[(index, tight, total)]
        return findNumbers(0, 1, 0)
