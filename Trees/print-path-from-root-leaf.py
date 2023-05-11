'''
Given a binary tree with distinct nodes(no two nodes have the same data values). The problem is to print the path from root to a given node x. If node x is not present then print “No Path”.

Examples: 

Input :          1
                /   \
                2     3
              /  \   /  \
            4    5  6   7
 x = 5
Output : 1->2->5
'''

from os import *
from sys import *
from collections import *
from math import *

from typing import List


class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathInATree(root: TreeNode, x: int) -> List[int]:
    path = []
    if not root:
        return path
    def findPath(root, path, x):
        path.append(root.data)
        if root.data == x:
            return True
        left = False
        if root.left:
            left = findPath(root.left, path, x)
        right = False
        if root.right:
            right = findPath(root.right, path, x)
        if left or right:
            return True
        else:
            path.pop()
            return False
    findPath(root, path, x)
    return path