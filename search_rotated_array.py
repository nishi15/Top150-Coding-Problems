'''
33. Search in Rotated Sorted Array
Medium

17069

1033

Add to List

Share
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

'''

class Solution:
    def search(self, nums, target: int) -> int:
        
        l = 0
        r = len(nums) -1
        
        while l <= r:
            mid = (l+r) //2
            print(mid)            
            if target == nums[mid]:
                return mid                     
            
            # search in left sorted array
            if nums[l] <= nums[mid]:

                #if the target in either greater than mid or target is less then left pointer 
                # we will move to right part of the arry
                # else -> stay at left part and search again
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                else:
                    r = mid -1

            # searching in the right sorted array
            else:

                # if target is less than mid ele or target is greater than right pointer 
                # we will move to left part of array
                # else -> stay at right part
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid +1

        return -1
        
        
if __name__ == "__main__":
    sol = Solution()
    print("-->",sol.search([4,5,6,7,8,1,2,3],8))