'''
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.lst = []
        def findInorder(root):
            if not root:
                return
            findInorder(root.left)
            self.lst.append(root.val)
            findInorder(root.right)

        findInorder(root)
        left, right = 0, len(self.lst) - 1

        print(self.lst)

        while left < right:
            sm = self.lst[left] + self.lst[right]
            if sm == k:
                return True
            elif sm < k:
                left += 1
            else:
                right -= 1

        return False