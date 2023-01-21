'''
Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree over the right subtree. 
Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.
Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Example 1:

Input:
        1 
      /   \
     2     3  
    / \   / \ 
   4   5 6   7
      / \
     8   9
   
Output: 1 2 4 8 9 6 7 3
'''

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        ans = []
        def isLeaf(root):
            if not root.left and not root.right:
                return True
            return False
            
        def leftBoundary(node):
            node = node.left
            while(node != None):
                if not isLeaf(node):
                    ans.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right
                    
        def rightBoundary(node):
            node = node.right
            tmp = []
            while(node != None):
                if not isLeaf(node):
                    tmp.append(node)
                if node.right:
                    node = node.right
                else:
                    node = node.left
                    
            while tmp:
                popped=tmp.pop()
                ans.append(popped.data)
                    
        def leafBoundary(root):
            if isLeaf(root):
                ans.append(root.data)
                
            if root.left:
                leafBoundary(root.left)
            if root.right:
                leafBoundary(root.right)
                    
                
                
        if not root:
            return self.ans
        if not isLeaf(root):
            ans.append(root.data)
        leftBoundary(root)
        leafBoundary(root)
        rightBoundary(root)
        
        return ans