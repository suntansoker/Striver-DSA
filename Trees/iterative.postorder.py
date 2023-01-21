'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
'''

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st1 = []
        st2 = []
        ans = []
        if not root:
            return ans
        st1.append(root)
        while st1:
            node = st1.pop()
            st2.append(node)
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        while st2:
            ans.append(st2.pop().val)

        return ans