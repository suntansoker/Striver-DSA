'''
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.timer = 0
        adj = defaultdict(list)
        for c in connections:
            adj[c[0]].append(c[1])
            adj[c[1]].append(c[0])

        def dfs(node, parent, vis, tin, low, ans):
            vis[node] = 1
            tin[node] = low[node] = self.timer
            self.timer += 1
            for it in adj[node]:
                if it==parent:
                    continue
                if vis[it] == 0:
                    dfs(it, node, vis, tin, low, ans)
                    low[node] = min(low[node], low[it])
                    if low[it] > tin[node]:
                        ans.append([node, it])
                else:
                    low[node] = min(low[node], low[it])

        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        ans = []
        dfs(0, -1, vis, tin, low, ans)
        return ans