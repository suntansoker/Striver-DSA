'''
Given a weighted, undirected and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

Example 1:

Input:
3 3
0 1 5
1 2 3
0 2 1

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Example 2:

Input:
2 1
0 1 5

Output:
5
Explanation:
Only one Spanning Tree is possible
which has a weight of 5.
'''

import heapq

class Solution:
    def spanningTree(self, V, adj):
        # PRIMS ALGORITHM
        # pq = []
        # vis = [0] * V
        # heapq.heappush(pq, (0,0,-1))
        # ans = 0
        
        # while pq:
        #     wt, node, parent = heapq.heappop(pq)
        #     if vis[node] == 1:
        #         continue
        #     else:
        #         vis[node] = 1
        #         ans += wt
        #         for adjNode in adj[node]:
        #             heapq.heappush(pq, (adjNode[1], adjNode[0], node))
                    
        # return ans

        # KRUSKAL ALGORITHM
        pq = []
        parent = [i for i in range(V)]
        rank = [0 for _ in range(V)]
        minDist = 0
        def findUParent(node):
            if node == parent[node]:
                return node
            parent[node] = findUParent(parent[node])
            return parent[node]
        def UnionByRank(node1, node2):
            ulp_node1 = findUParent(node1)
            ulp_node2 = findUParent(node2)
            if ulp_node1 == ulp_node2:
                return
            if rank[ulp_node1] < rank[ulp_node2]:
                parent[ulp_node1] = ulp_node2
            elif rank[ulp_node2] < rank[ulp_node1]:
                parent[ulp_node2] = ulp_node1
            else:
                parent[ulp_node2] = ulp_node1
                rank[ulp_node1] += 1
        for i in range(V):
            for it in adj[i]:
                node = i
                adjNode = it[0]
                wt = it[1]
                heapq.heappush(pq, (wt, node, adjNode))
                
        while pq:
            weight, node1, node2 = heapq.heappop(pq)
            ulp_1 = findUParent(node1)
            ulp_2 = findUParent(node2)
            
            if ulp_1 != ulp_2:
                UnionByRank(node1, node2)
                minDist += weight
                
        return minDist
        