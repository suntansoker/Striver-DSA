'''
Given a tree with N nodes, return a tree with the children sum property such that the parent mode is the sum of the children nodes
'''

from os import *
from sys import *
from collections import *
from math import *

'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
        
def changeTree(root): 
    if not root:
        return
    sm = 0
    if root.left:
        sm += root.left.data
    if root.right:
        sm += root.right.data
    if sm >= root.data:
        root.data = sm
    else:
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data
            
    changeTree(root.left)
    changeTree(root.right)
    
    sm = 0
    if root.left:
        sm += root.left.data
    if root.right:
        sm += root.right.data
        
    if sm>0:
        root.data = sm