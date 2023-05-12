'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key= len)
        n = len(words)
        dp = [1] * n
        mx = 1
        lastIndex = 0
        def isPossible(str1, str2):
            if len(str1) != len(str2) + 1:
                return False
            count = 0
            idx1 = 0
            idx2 = 0
            while idx1<len(str1):
                if idx2 < len(str2) and str1[idx1] == str2[idx2]:
                        idx1 += 1
                        idx2 += 1
                else:
                    idx1 += 1

            if idx1 == len(str1) and idx2 == len(str2):
                return True
            else:
                return False

        for index in range(n):
            for prev in range(index):
                if isPossible(words[index], words[prev]) and 1 + dp[prev] > dp[index]:
                    dp[index] = 1 + dp[prev]

            if dp[index] > mx:
                mx = dp[index]
                lastIndex = index

        return mx