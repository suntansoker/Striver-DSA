from os import *
from sys import *
from collections import *
from math import *

from typing import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isEnd = True

    def ifPrefixExists(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
            if not node.isEnd:
                return False

        return True
            
def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    for i in range(n):
        trie.insert(a[i])

    res = ""
    for w in a:
        if trie.ifPrefixExists(w):
            if len(w) > len(res):
                res = w
            elif len(w) == len(res):
                if w<res:
                    res = w

    if len(res) == 0:
        return "None"
    else:
        return res

    