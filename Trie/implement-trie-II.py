'''
 Implement a data structure ”TRIE” from scratch. Complete some functions.

1) Trie(): Initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Delete this string “WORD” from the “TRIE”.
'''

from os import *
from sys import *
from collections import *
from math import *
class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
        self.pCount = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
            node.pCount += 1
        node.count += 1


    def countWordsEqualTo(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return 0
            node = node.children[w]

        return node.count

    def countWordsStartingWith(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return 0
            node = node.children[w]

        return node.pCount

    def erase(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return
            node = node.children[w]
            node.pCount -= 1

        node.count -= 1
        return
