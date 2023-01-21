'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        if root == None:
            return self.ans

        leftToRight = True
        q = []
        q.append(root)

        while q:
            n = len(q)
            res = [0] * n
            for i in range(n):
                node = q.pop(0)
                if leftToRight:
                    idx = i
                else:
                    idx = n - i - 1
                res[idx] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            leftToRight = not leftToRight
            self.ans.append(res)
        
        return self.ans

