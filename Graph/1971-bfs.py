# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = [0] * n
        adj = defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])

        q = []
        q.append(source)
        vis[source] = 1

        while q:
            ele = q.pop(0)
            if ele == destination:
                return True
            
            for it in adj[ele]:
                if vis[it] == 0:
                    q.append(it)
                    vis[it] = 1

        return False