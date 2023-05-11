# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        vis = [[0] * n for _ in range(m)]

        def dfs(i, j, vis, board):
            nonlocal m, n
            vis[i][j] = 1
            dir = [[0,-1], [0, 1], [1, 0], [-1, 0]]
            for d in dir:
                x = i + d[0]
                y = j + d[1]
                if x>=0 and x<m and y>=0 and y<n and vis[x][y] == 0 and board[x][y] == "O":
                    dfs(x, y, vis, board)

            return
        for i in range(m):
            if board[i][0] == "O" and vis[i][0] == 0:
                dfs(i, 0, vis, board)

        for i in range(n):
            if board[m-1][i] == "O" and vis[m-1][i] == 0:
                dfs(m-1, i, vis, board)

        for i in range(m-1, -1, -1):
            if board[i][n-1] == "O" and vis[i][n-1] == 0:
                dfs(i, n-1, vis, board)

        for i in range(n):
            if board[0][i] == "O" and vis[0][i] == 0:
                dfs(0, i, vis, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and vis[i][j] == 0:
                    board[i][j] = "X"

        return board