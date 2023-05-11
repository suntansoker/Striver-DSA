'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode], isReverse):
        self.st = []
        self.isReverse = isReverse
        while root:
            self.st.append(root)
            if not self.isReverse:
                root = root.left
            else:
                root = root.right
        

    def next(self) -> int:
        if len(self.st) > 0:
            node = self.st.pop()
            value = node.val
            if not self.isReverse:
                node = node.right
                while node:
                    self.st.append(node)
                    node = node.left
                return value
            else:
                node = node.left
                while node:
                    self.st.append(node)
                    node = node.right
                return value
        return None
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # TWO POINTERS WITH CACHE (Space complexity: O(n))
        # self.lst = []
        # def findInorder(root):
        #     if not root:
        #         return
        #     findInorder(root.left)
        #     self.lst.append(root.val)
        #     findInorder(root.right)

        # findInorder(root)
        # left, right = 0, len(self.lst) - 1

        # print(self.lst)

        # while left < right:
        #     sm = self.lst[left] + self.lst[right]
        #     if sm == k:
        #         return True
        #     elif sm < k:
        #         left += 1
        #     else:
        #         right -= 1

        # return False

        # Using BST Iterator (Space complexity: O(1)) 
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)

        left = l.next()
        right = r.next()

        while left < right:
            sm = left + right
            if sm == k:
                return True
            elif sm < k:
                left = l.next()
            else:
                right = r.next()

        return False