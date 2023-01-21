'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mp = {}
        vis = set()
        self.ans = []
        def getParent(node, parent):
            if not node:
                return
            mp[node] = parent
            if node.left:
                getParent(node.left, node)
            if node.right:
                getParent(node.right, node)
        def getNodes(node, cnt):
            if not node or node in vis or cnt>k:
                return
            if cnt == k:
                self.ans.append(node.val)
            vis.add(node)
            if node.left:
                getNodes(node.left, cnt + 1)
            if node.right:
                getNodes(node.right, cnt + 1)
            getNodes(mp[node], cnt + 1)
            

        getParent(root, None)
        getNodes(target, 0)
        return self.ans
