'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
'''

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        ans = []
        if not root:
            return ans
        st.append(root)
        while st:
            node = st.pop()
            ans.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return ans