'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
'''

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        size = [1] * (n*n)
        parent = [i for i in range(n*n)]
        
        def findUParent(node):
            if node == parent[node]:
                return node
            parent[node] = findUParent(parent[node])
            return parent[node]

        def UnionBySize(node1, node2):
            ulp1 = findUParent(node1)
            ulp2 = findUParent(node2)

            if ulp1 == ulp2:
                return

            if size[ulp1] < size[ulp2]:
                parent[ulp1] = ulp2
                size[ulp2] += size[ulp1]

            else:
                parent[ulp2] = ulp1
                size[ulp1] += size[ulp2]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                node = n * i + j
                dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for d in dir:
                    x = i + d[0]
                    y = j + d[1]
                    adjNode = x * n + y
                    if x>=0 and x<n and y>=0 and y<n and grid[x][y] == 1:
                        UnionBySize(node, adjNode)

        mx = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                node = n * i + j
                dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                comps = set()
                for d in dir:
                    x = i + d[0]
                    y = j + d[1]
                    adjNode = x * n + y
                    if x>=0 and x<n and y>=0 and y<n and grid[x][y] == 1:
                        comps.add(findUParent(adjNode))
                sm = 0
                for par in list(comps):
                    sm += size[par]
                mx = max(mx, sm+1)

        for cell in range(0, n*n):
            mx = max(mx, size[findUParent(cell)])

        return mx

                    



        