# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


# Example 1:

# Input:

# Output: 1
# Explanation: 3 -> 3 is a cycle

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        inDegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1
                
        q = []
        topo = []
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
                
        while q:
            popped = q.pop(0)
            topo.append(popped)
            for it in adj[popped]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    q.append(it)
                    
        if len(topo) == V:
            return 0
        else:
            return 1