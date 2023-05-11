# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        ans  = [[0] * c for _ in range(r)]
        maxTime = 0
        q = []
        for i in range(r):
            for j in range(c):
                ans[i][j] = grid[i][j]
                if ans[i][j] == 2:
                    q.append((i, j, 0))

        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            popped = q.pop(0)
            x = popped[0]
            y = popped[1]
            prev_time = popped[2]

            for d in dir:
                x_new = x + d[0]
                y_new = y + d[1]
                new_time = prev_time + 1
                if x_new>=0 and x_new<r and y_new>=0 and y_new<c and grid[x_new][y_new] == 1 and ans[x_new][y_new] != 2:
                    ans[x_new][y_new] = 2
                    q.append((x_new, y_new, new_time))
                    maxTime = max(maxTime, new_time)

        for i in range(r):
            for j in range(c):
                if ans[i][j] == 1:
                    return -1

        return maxTime


