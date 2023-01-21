#User function Template for python3
from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n, m, edges):
        res = [10 ** 9] * (n+1)
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))
            
        parent = [0] * (n+1)
        for i in range(n+1):
            parent[i] = i
            
        res[1] = 0
        pq = []
        heapq.heappush(pq, (0, 1))
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            for it in adj[node]:
                adjNode = it[0]
                weight = it[1]
                
                if dist + weight < res[adjNode]:
                    res[adjNode] = dist + weight
                    parent[adjNode] = node
                    heapq.heappush(pq, (res[adjNode], adjNode))
           
        if res[n] == 10 ** 9:
            return [-1]
        i = n
        an = []
        while i != parent[i]:
            an.append(i)
            i = parent[i]
            
        an.append(1)
            
        return reversed(an)