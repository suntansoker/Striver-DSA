# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeftHeight(self,root):
            if not root:
                return 0
            count = 1
            while(root.left):
                count += 1
                root = root.left

            return count

    def findRightHeight(self,root):
        if not root:
            return 0
        count = 1
        while(root.right):
            count += 1
            root = root.right

        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.findLeftHeight(root)
        r = self.findRightHeight(root)

        if l==r:
            return 2**l - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)