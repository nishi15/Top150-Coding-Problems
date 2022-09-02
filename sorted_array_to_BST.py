'''
108. Convert Sorted Array to Binary Search Tree
Easy

8045

403

Add to List

Share
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
Accepted
858,363
Submissions
1,253,304

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):        
        
        if not nums:
            # print(nums[0])
            return None

        mid = len(nums)//2
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        
        return TreeNode(
            nums[mid],left,right
        )

        
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.sortedArrayToBST([10,11,12,13,14,15,16,17,18,19])
    print("Result :")
    print(res.val,res.left,res.right)
        
