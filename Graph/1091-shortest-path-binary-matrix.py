'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dis = [[10 ** 9] * n for _ in range(n)]

        if grid[0][0] != 0:
            return -1

        dis[0][0] = 1

        q = []
        q.append((1,0,0))
        
        dir = [[0,1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        while q:
            dist, node_x, node_y = q.pop(0)
            for x, y in dir:
                adj_x = node_x + x
                adj_y = node_y + y
                if adj_x>=0 and adj_x<n and adj_y>=0 and adj_y<n and grid[adj_x][adj_y] == 0 and dist + 1 < dis[adj_x][adj_y]:
                    dis[adj_x][adj_y] = dist + 1
                    q.append((dis[adj_x][adj_y], adj_x, adj_y))
                    
        if dis[n-1][n-1] == 10 ** 9:
            return -1

        return dis[n-1][n-1]