class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        r = len(isConnected)
        c = len(isConnected[0])

        # DFS WITH CONNECTED COMPONENTS
        # adjList = defaultdict(list)
        # for i in range(r):
        #     for j in range(c):
        #         if isConnected[i][j] == 1:
        #             adjList[i].append(j)
        #             adjList[j].append(i)

        # count = 0
        # vis = [0] * r

        # def dfs(node, vis, adjList):
        #     vis[node] = 1
        #     for it in adjList[node]:
        #         if vis[it] == 0:
        #             dfs(it, vis, adjList)
        #     return
            
        # for i in range(r):
        #     if vis[i] == 0:
        #         count += 1
        #         dfs(i, vis, adjList)

        # return count

        # DISJOINT SETS
        pq = []
        parent = [i for i in range(r)]
        rank = [0 for _ in range(r)]
        minDist = 0
        def findUParent(node):
            if node == parent[node]:
                return node
            parent[node] = findUParent(parent[node])
            return parent[node]
        def UnionByRank(node1, node2):
            ulp_node1 = findUParent(node1)
            ulp_node2 = findUParent(node2)
            if ulp_node1 == ulp_node2:
                return
            if rank[ulp_node1] < rank[ulp_node2]:
                parent[ulp_node1] = ulp_node2
            elif rank[ulp_node2] < rank[ulp_node1]:
                parent[ulp_node2] = ulp_node1
            else:
                parent[ulp_node2] = ulp_node1
                rank[ulp_node1] += 1
        for i in range(r):
            for j in range(c):
                if isConnected[i][j] == 1:
                    UnionByRank(i, j)
        cnt = 0
        for i in range(r):
            if parent[i] == i:
                cnt += 1

        return cnt
            