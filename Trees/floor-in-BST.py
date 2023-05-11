    # https://bit.ly/3svQMi1
    
    # Following is the TreeNode class structure

    # class TreeNode:

    #     def __init__ (self, data):

    #         self.data = data
    #         self.left = None
    #         self.right = None



def floorInBST(root, X):
    node = None
    def findFloorNode(root, X):
        nonlocal node
        while root:
            if root.data == X:
                return root
            if root.data > X:
                root = root.left
            else:
                node = root
                root = root.right
                
        return node
    
    node = findFloorNode(root, X)
    if not node:
        return -1
    return node.data