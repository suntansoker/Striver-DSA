# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

# Example 1:


# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[0] * n for _ in range(m)]

        def dfs(i, j, vis, grid):
            # nonlocal m, n
            vis[i][j] = 1
            dir = [[0,-1], [0, 1], [1, 0], [-1, 0]]
            for d in dir:
                x = i + d[0]
                y = j + d[1]
                if x>=0 and x<m and y>=0 and y<n and vis[x][y] == 0 and grid[x][y] == 1:
                    dfs(x, y, vis, grid)
                    
        for i in range(m):
            if grid[i][0] == 1 and vis[i][0] == 0:
                dfs(i, 0, vis, grid)

        for i in range(n):
            if grid[m-1][i] == 1 and vis[m-1][i] == 0:
                dfs(m-1, i, vis, grid)

        for i in range(m-1, -1, -1):
            if grid[i][n-1] == 1 and vis[i][n-1] == 0:
                dfs(i, n-1, vis, grid)

        for i in range(n):
            if grid[0][i] == 1 and vis[0][i] == 0:
                dfs(0, i, vis, grid)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    count += 1

        return count