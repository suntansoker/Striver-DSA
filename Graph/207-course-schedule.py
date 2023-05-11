# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        inDegree = [0] * numCourses

        for k in range(numCourses):
            for it in adj[k]:
                inDegree[it] += 1

        q=[]
        topo = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            popped = q.pop(0)
            topo.append(popped)

            for it in adj[popped]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    q.append(it)

        if len(topo) < numCourses:
            return False
        else:
            return True


    

        
