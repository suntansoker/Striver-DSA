# Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.
# Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
 

# Example 1:

# Input: 
# N = 5, K = 4
# dict = {"baa","abcd","abca","cab","cad"}
# Output:
# 1
# Explanation:
# Here order of characters is 
# 'b', 'd', 'a', 'c' Note that words are sorted 
# and in the given language "baa" comes before 
# "abcd", therefore 'b' is before 'a' in output.
# Similarly we can find other orders.

from collections import defaultdict
class Solution:
    def findOrder(self,dict, N, K):
        adj = defaultdict(list)
        
        def topoSort(V, adj):
            inDegree = [0] * V
            topo = []
            for i in range(V):
                for it in adj[i]:
                    inDegree[it] += 1
                    
            q = []
            for i in range(V):
                if inDegree[i] == 0:
                    q.append(i)
                    
            while q:
                node = q.pop(0)
                topo.append(node)
                for it in adj[node]:
                    inDegree[it] -= 1
                    if inDegree[it] == 0:
                        q.append(it)
                        
            return topo
                    
        for i in range(N-1):
            str1 = dict[i]
            str2 = dict[i+1]
            l = min(len(str1), len(str2))
            for j in range(l):
                if str1[j] != str2[j]:
                    adj[ord(str1[j]) - ord('a')].append(ord(str2[j]) - ord('a'))
                    break
                    
        lst = topoSort(K, adj)
        st = ""
        for i in range(len(lst)):
            st = st + chr(ord('a') + lst[i])
            
        return st