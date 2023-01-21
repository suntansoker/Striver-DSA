'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        st = []
        node = root
        while True:
            if node:
                st.append(node)
                node = node.left
            else:
                if not st:
                    break
                node = st.pop()
                ans.append(node.val)
                node = node.right

        return ans