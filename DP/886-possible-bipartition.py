# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

# Example 1:

# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4] and group2 [2,3].

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for i in range(len(dislikes)):
            adjList[dislikes[i][0]].append(dislikes[i][1])
            adjList[dislikes[i][1]].append(dislikes[i][0])

        grpArray = [-1] * (n+1)

        def dfs(node, adjList, grpArray, grp):
            grpArray[node] = grp

            for it in adjList[node]:
                if grpArray[it] == -1:
                    if dfs(it, adjList, grpArray, 1-grp) == False:
                        return False
                elif grpArray[it] == grp:
                        return False

            
            return True

        for i in range(1, n+1):
            if grpArray[i] == -1:
                if dfs(i, adjList, grpArray, 0) == False:
                    return False

        return True
