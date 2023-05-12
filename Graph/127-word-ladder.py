# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = []
        wordSet = set(wordList)

        q.append((beginWord, 1))
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while q:
            popped = q.pop(0)
            word = popped[0]
            no = popped[1]
            if word == endWord:
                return no
            for i in range(len(word)):
                orig = word[i]
                for ch in range(ord('a'), ord('z')+1):
                    lst = list(word)
                    lst[i] = chr(ch)
                    word = "".join(lst)
                    if word in wordSet:
                        q.append((word, no + 1))
                        wordSet.remove(word)
                lst1 = list(word)
                lst1[i] = orig
                word = "".join(lst1)

        return 0


