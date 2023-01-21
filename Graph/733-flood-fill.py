# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        ans = [[0] * c for _ in range(r)] 
        for i in range(r):
            for j in range(c):
                ans[i][j] = image[i][j]

        oldColor = image[sr][sc]
        ans[sr][sc] = color
        q = []
        q.append((sr, sc))

        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            popped = q.pop(0)
            popped_x = popped[0]
            popped_y = popped[1]
            for d in dir:
                x_new = popped_x + d[0]
                y_new = popped_y + d[1]
                if x_new>=0 and x_new <r and y_new>=0 and y_new<c and image[x_new][y_new] == oldColor and ans[x_new][y_new] != color:
                    ans[x_new][y_new] = color
                    q.append((x_new, y_new))

        return ans