'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        extraEdges = 0
        parent = [i for i in range(n)]
        rank = [0] * n
        def findUParent(node):
            if parent[node] == node:
                return node
            parent[node] = findUParent(parent[node])
            return parent[node]

        def UnionByRank(node1, node2):
            ulp1 = findUParent(node1)
            ulp2 = findUParent(node2)
            if rank[ulp1] < rank[ulp2]:
                parent[ulp1] = ulp2
            elif rank[ulp2] < rank[ulp1]:
                parent[ulp2] = ulp1
            else:
                parent[ulp2] = ulp1
                rank[ulp1] += 1

        for it in connections:
            node1 = it[0]
            node2 = it[1]

            if findUParent(node1) ==findUParent(node2):
                extraEdges += 1
            else:
                UnionByRank(node1, node2)

        countComp = 0
        for i in range(n):
            if parent[i] == i:
                countComp += 1

        if extraEdges >= countComp - 1:
            return countComp - 1
        
        return -1