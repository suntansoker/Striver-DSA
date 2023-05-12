'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.
 

Example 1:

Input:

Output:
3
Explanation:

We can clearly see that there are 3 Strongly
Connected Components in the Graph
Example 2:

Input:

Output:
1
Explanation:
All of the nodes are connected to each other.
So, there's only one SCC.
'''

from collections import defaultdict
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        vis = [0] * V
        st = []
        def dfs(ind, adj, vis, q):
            vis[ind] = 1
            for it in adj[ind]:
                if vis[it] == 0:
                    dfs(it, adj, vis, q)
            st.append(ind)
            
        def dfs2(index, adj2, vis):
            vis[index] = 1
            for it in adj2[index]:
                if vis[it] == 0:
                    dfs2(it, adj2, vis)
            
        for i in range(V):
            if vis[i] == 0:
                dfs(i, adj, vis, st)
                
        adj2 = defaultdict(list)
        for ind in range(V):
            for it in adj[ind]:
                adj2[it].append(ind)
                
        for i in range(V):
            vis[i] = 0
            
        cnt = 0
        while st:
            node = st.pop()
            if vis[node] == 0:
                cnt += 1
                dfs2(node, adj2, vis)
                
        return cnt