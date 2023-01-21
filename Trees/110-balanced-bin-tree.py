# Given a binary tree, determine if it is 
# height-balanced.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = 0
        if root.left:
            left = self.maxDepth(root.left)
        right = 0
        if root.right:
            right = self.maxDepth(root.right)
        return 1+max(left, right)

    def isBalanced(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return True
        lHeight = self.maxDepth(node.left)
        rHeight = self.maxDepth(node.right)
        if abs(lHeight - rHeight) > 1:
            return False
        
        left = self.isBalanced(node.left)
        right = self.isBalanced(node.right)

        if not left or not right:
            return False

        return True