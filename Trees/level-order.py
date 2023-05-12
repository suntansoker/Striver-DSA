'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level). 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
//Commenting
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        ans = []
        if root is None:
            return ans
        q.append(root)
        while q:
            count = len(q)
            res = []
            while count > 0:
                node = q.pop(0)
                count -= 1
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(res[:])

        return ans