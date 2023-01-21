# Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

# Example 1:

# Input:

# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 3, 2, 1, 0.

class Solution: 
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # DFS
        # vis = [0] * V
        # topList = []
        
        # def dfs(index, vis, adj, topList):
        #     vis[index] = 1
        #     for it in adj[index]:
        #         if vis[it] == 0:
        #             dfs(it, vis, adj, topList)
                    
        #     topList.append(index)
        # for i in range(V):
        #     if vis[i] == 0:
        #         dfs(i, vis, adj, topList)
                
        # ans = []
        # for i in range(len(topList)-1, -1, -1):
        #     ans.append(topList[i])
                
        # return ans

        # BFS
        inComing = [0] * V
        for i in range(V):
            for it in adj[i]:
                inComing[it] += 1
                
        q = []
        for i in range(V):
            if inComing[i] == 0:
                q.append(i)
                
        topo = []
                
        while q:
            popped = q.pop(0)
            topo.append(popped)
            
            for it in adj[popped]:
                inComing[it] -= 1
                if inComing[it] == 0:
                    q.append(it)
                    
        return topo