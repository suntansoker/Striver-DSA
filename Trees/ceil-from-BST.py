# https://bit.ly/3AYpF24

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    node = None
    def findCeilNode(root, x):
        nonlocal node
        while root:
            if root.data == x:
                return root
            if root.data < x:
                root = root.right
            else:
                node = root
                root = root.left
        return node
    
    node = findCeilNode(root, x)
    if node:
        return node.data
    return -1