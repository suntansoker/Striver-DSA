'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell. 

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
'''

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        dis = [[10 ** 9] * n for _ in range(m)]

        dis[0][0] = 0

        q = []
        q.append((0,0,0))
        
        dir = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while q:
            dist, node_x, node_y = heapq.heappop(q)
            if node_x == m-1 and node_y == n-1:
                return dis[m-1][n-1]
            for x, y in dir:
                adj_x = node_x + x
                adj_y = node_y + y
                if adj_x>=0 and adj_x<m and adj_y>=0 and adj_y<n:
                    maxDistance = max(abs(heights[adj_x][adj_y] - heights[node_x][node_y]), dist)
                    if maxDistance < dis[adj_x][adj_y]:
                        dis[adj_x][adj_y] = maxDistance
                        heapq.heappush(q, (dis[adj_x][adj_y], adj_x, adj_y))
                    
        return dis[m-1][n-1]