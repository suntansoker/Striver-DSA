'''
Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i, 0<=i

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

Example:

Input:
n = 6, m= 7
edge=[[0,1,2],[0,4,1],[4,5,4]
,[4,2,2],[1,2,3],[2,3,6],[5,3,1]]

Output:
0 2 3 6 1 5
'''

from typing import List
from collections import defaultdict

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        def topoSort(node, vis, adj, st):
            vis[node] = 1
            for it in adj[node]:
                if vis[it[0]] == 0:
                    topoSort(it[0], vis, adj, st)
                    
            st.append(node)
        adj = defaultdict(list)
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            
            adj[u].append((v, wt))
            
        MAX = 10 ** 9
        vis = [0] * n
        st = []
        for i in range(n):
            if vis[i] == 0:
                topoSort(i, vis, adj, st)
                
        dist = [MAX] * n
        dist[0] = 0
        
        while st:
            node = st.pop()
            
            for it in adj[node]:
                v = it[0]
                wt = it[1]
                
                if dist[v] > dist[node] + wt:
                    dist[v] = dist[node] + wt
                    
        for i in range(n):
            if dist[i] == MAX:
                dist[i] = -1
                
        return dist