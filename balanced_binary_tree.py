'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

'''

import tree_helper
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        left = right = 0
        res = self._isBalanced(root)
        return res[0]

    def _isBalanced(self,node):
        if not node:
            return [True,0]
        
        left_height = self._isBalanced(node.left)
        right_height = self._isBalanced(node.right)
        balanced = left_height[0] and right_height[0] and (abs(left_height[1]-right_height[1])<=1)

        return [balanced,1+max(left_height[1],right_height[1])]
        


if __name__ == "__main__":
    root = tree_helper.Tree()
    root.insert_node([3,2,20,18,17])
    head = root.show_tree()

    sol = Solution()
    print(sol.isBalanced(head))
