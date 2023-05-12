class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isEnd = {}
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, num):
                node = self.root
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if bit not in node.children:
                        node.children[bit] = TrieNode()
                    node = node.children[bit]
                node.isEnd = True

            def getMax(self, num):
                node = self.root
                mx = 0
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if (1-bit) in node.children:
                        mx = mx | (1 << i)
                        node = node.children[1-bit]
                    else:
                        node = node.children[bit]
                return mx
                
        trie = Trie()
        mxNum = 0
        for n in nums:
            trie.insert(n)
        for num in nums:
            n = trie.getMax(num)
            mxNum = max(mxNum, n)

        return mxNum
            

