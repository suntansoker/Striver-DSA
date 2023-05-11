'''
Given a string of alphabetic characters. Return the count of distinct substrings of the string(including the empty string) using the Trie data structure.

Examples:

Example 1:
Input:
 S1= “ababa”
Output: Total number of distinct substrings : 10
Explanation: All the substrings of the string are a, ab, aba, abab, ababa, b, ba, bab, baba, a, ab, aba, b, ba, a. Many of the substrings are duplicated. The distinct substrings are a, ab, aba, abab, ababa, b, ba, bab, baba. Total Count of the distinct substrings is 9 + 1(for empty string) = 10.

'''

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

def countDistinctSubstrings(s):
    root = TrieNode()
    count = 0
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            if s[j] not in node.children:
                node.children[s[j]] = TrieNode()
                count += 1
            node = node.children[s[j]]

    return count + 1