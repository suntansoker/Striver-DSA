'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.ans = 0
        def findkthSmallest(root, k):
            if not root:
                return
            findkthSmallest(root.left, k)
            self.cnt += 1
            if self.cnt == k:
                self.ans =  root.val
                return
            findkthSmallest(root.right, k)
        findkthSmallest(root, k)
        return self.ans