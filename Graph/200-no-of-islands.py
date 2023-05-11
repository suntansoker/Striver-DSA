# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        count = 0
        def bfs(row, col, visited, grid):
            visited[row][col] = True
            q = []
            q.append((row, col))

            while len(q)>0:
                ele = q.pop(0)
                first = ele[0]
                second = ele[1]
                ranges = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for i in range(len(ranges)):
                    x = first + ranges[i][0]
                    y = second + ranges[i][1]
                    if (x>=0 and x<len(grid) and y>=0 and y<len(grid[0])
                    and not visited[x][y] and grid[x][y] == "1"):
                        visited[x][y] = True
                        q.append((x, y))


        for i in range(m):
            for j in range(n):
                if(not visited[i][j] and grid[i][j] == "1"):
                    count += 1
                    bfs(i, j, visited, grid)

        return count
