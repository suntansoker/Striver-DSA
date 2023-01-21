# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

# Count the number of distinct islands. An island is considered to be the same as another if and only if one island has the same shape as another island (and not rotated or reflected).

# Example
# Example 1:

# Input: 
#   [
#     [1,1,0,0,1],
#     [1,0,0,0,0],
#     [1,1,0,0,1],
#     [0,1,0,1,1]
#   ]
# Output: 3
# Explanation:
#   11   1    1
#   1        11   
#   11
#    1
# Example 2:

# Input:
#   [
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [0,0,0,1,1],
#     [0,0,0,1,1]
#   ]
# Output: 1

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[0] * n for _ in range(m)]
        st = set()

        def dfs(i, j, vis, grid, basei, basej, lst):
            nonlocal m, n
            vis[i][j] = 1
            lst.append((i-basei, j - basej))

            dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for d in dir:
                x = i + d[0]
                y = j + d[1]
                if x>=0 and x<m and y>=0 and y<n and vis[x][y] == 0 and grid[x][y] == 1:
                    dfs(x, y, vis, grid, basei, basej, lst)

            return


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    lst = []
                    dfs(i, j, vis, grid, i, j, lst)
                    st.add(tuple(lst))
                    

        return len(st)