'''
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.You need to return an array of size K.

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Example
Example 1:

Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
'''

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        parent = [i for i in range(n * m)]
        rank = [0 for _ in range(n * m)]
        vis = [[0] * m for _ in range(n)]

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

        cnt = 0
        ans = []
        for operator in operators:
            u, v = operator.x, operator.y
            if vis[u][v] == 1:
                ans.append(cnt)
                continue
            vis[u][v] = 1
            d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            cnt += 1

            node = m * u + v

            for each in d:
                x = u + each[0]
                y = v + each[1]

                if x>=0 and x<n and y>=0 and y<m and vis[x][y] == 1:
                    adjNode = m * x + y
                    if findUParent(node) != findUParent(adjNode):
                        cnt -= 1
                        UnionByRank(node, adjNode)

            ans.append(cnt)

        return ans
