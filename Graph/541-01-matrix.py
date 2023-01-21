# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Example 1:

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = []
        r = len(mat)
        c = len(mat[0])
        ans = [[0] * c for _ in range(r)]
        vis = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                ans[i][j] = mat[i][j]
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    vis[i][j] = 1

        dir = [[-1, 0], [1, 0], [0,1], [0, -1]]
        while q:
            x, y, dist = q.pop(0)
            for d in dir:
                x_new = x + d[0]
                y_new = y + d[1]
                new_dist = dist + 1
                if x_new >=0 and x_new < r and y_new >=0 and y_new < c and vis[x_new][y_new] == 0:
                    q.append((x_new, y_new, new_dist))
                    vis[x_new][y_new] = 1
                    ans[x_new][y_new] = new_dist

        return ans


