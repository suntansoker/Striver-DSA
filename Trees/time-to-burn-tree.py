# https://bit.ly/3z3YEJY

class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None

def timeToBurnTree(root, start):
    vis = set()
    mp = {}
    timer = 0
    startNode = BinaryTreeNode(start)
    
    def getParent(node, parent):
        if not node:
            return
        mp[node] = parent
        if node.left:
            getParent(node.left, node)
        if node.right:
            getParent(node.right, node)
            
    def findStartNode(root, start):
        nonlocal startNode
        if not root:
            return
        if root.data == start:
            startNode = root
            return
        findStartNode(root.left, start)
        findStartNode(root.right, start)
            
        
    def getTime(q, vis):
        nonlocal timer
        while q:
            n = len(q)
            burn = False
            while n > 0:
                popped = q.pop(0)
                vis.add(popped)
                if popped.left:
                    burn = True
                    q.append(popped.left)
                if popped.right:
                    burn = True
                    q.append(popped.right)
                if mp[popped] and mp[popped] not in vis:
                    burn = True
                    q.append(mp[popped])
                n -= 1
                
            if burn:
                timer += 1
        
        
    getParent(root, None)
    findStartNode(root, start)
    q = []
    q.append(startNode)
    getTime(q, vis)
    return timer