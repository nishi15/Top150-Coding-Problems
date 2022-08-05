'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        # if root is empty , then return False
        if not root :
            return False

        # if subroot is empty , then return True -> as Null will always be the subtree of the root
        if not subRoot:
            return True

        # helper function used to compare subtrees 
        if self.isSametree(root,subRoot):
            return True

        # if root node not maching with root of subtree , 
        # then we move to left and right to match the subtree form root tree
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSametree(self,root,subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.isSametree(root.left,subRoot.left) and self.isSametree(root.right,subRoot.right)

        else:
            False


if __name__ == "__main__":
    sol = Solution()
    sol.isSubtree(root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2])