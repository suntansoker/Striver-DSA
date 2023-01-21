# Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 

# Example 1:

# Input:  
# V = 5, E = 5
# adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
# Output: 1
# Explanation: 

# 1->2->3->4->1 is a cycle.

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    vis = [0] * V
	   # BFS
	   # def findCycle(node, vis):
	   #     vis[node] = 1
	   #     q = []
	   #     q.append((node, -1))
	   #     while q:
	   #         nodes = q.pop(0)
	   #         curr = nodes[0]
	   #         parent = nodes[1]
	   #         for neighbour in adj[curr]:
	   #             if vis[neighbour] == 0:
	   #                 q.append((neighbour, curr))
	   #                 vis[neighbour] = 1
	   #             else:
	   #                 if neighbour != parent:
	   #                     return True
	                        
	   #     return False
	       
	   # for i in range(V):
	   #     if vis[i] == 0:
	   #         if findCycle(i, vis) == True:
	   #             return 1
	   # return 0
	   
	   # DFS
	    def findCycle(node, parent, vis):
	        vis[node] = 1
	        for neighbour in adj[node]:
	            if vis[neighbour] == 0:
	                if findCycle(neighbour, node, vis) == True:
	                    return True
	            else:
	                if neighbour != parent:
	                    return True
	                    
	        return False
	       
	    for i in range(V):
	        if vis[i] == 0:
	            if findCycle(i, -1, vis) == True:
	                return 1
	    return 0