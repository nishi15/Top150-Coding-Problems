'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        '''
        Inorder traversal :- Left ->Root ->Right
        '''
        if not root:
            return None
        
        li = []
        self.show(root,li)
        return li
    
    def show(self,node,li):
        if not node:
            return None
        
        # getting the left child
        left = self.show(node.left,li)

        # if there is left child append to list
        if left:
            li.append(left.val)
        
        # append parent node
        li.append(node.val)
        right = self.show(node.right,li)

        # if there is right child append to list
        if right:
            li.append(right.val)
