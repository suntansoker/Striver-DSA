'''
You are given an Undirected Graph having unit weight, Find the shortest path from src(0) to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Example:

Input:
n = 9, m= 10
edges=[[0,1],[0,3],[3,4],[4 ,5]
,[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
Output:
0 1 2 1 2 3 3 4 4
'''

from collections import defaultdict
class Solution:
    def shortestPath(self, edges, n, m, src):
        MAX = 10 ** 9
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        dist = [MAX] * n
        dist[src] = 0
        q = []
        q.append(src)
        
        while q:
            ele = q.pop()
            for it in adj[ele]:
                if dist[it] > 1 + dist[ele]:
                    dist[it] = 1 + dist[ele]
                    q.append(it)
                    
        for i in range(n):
            if dist[i] == MAX:
                dist[i] = -1
                
        return dist