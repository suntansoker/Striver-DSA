# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

# Example 1:

# Illustration of graph
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        adj = defaultdict(list)
        for i in range(V):
            for each in graph[i]:
                adj[each].append(i)

        inDegree = [0] * V
        q = []
        res = []

        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1

        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            popped = q.pop(0)
            res.append(popped)

            for it in adj[popped]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    q.append(it)

        res.sort()

        return res