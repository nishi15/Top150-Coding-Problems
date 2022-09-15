'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

'''
import tree_helper
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        maxsum = [0]        
    
        def helper(root):
            if not root:
                return 0

            left = helper(root.left) 
            right = helper(root.right)
            
            maxsum[0] = max(maxsum[0],left+right) # diameter
            return 1 + max(left,right) # hright

        
        helper(root)
        return maxsum[0]


if __name__ == "__main__":
    sol = Solution()
    tree = tree_helper.Tree()
    tree.insert_node([1,2,3,4,5])
    root = tree.show_tree()
    res = sol.diameterOfBinaryTree(root)
    print("Diameter",res)
