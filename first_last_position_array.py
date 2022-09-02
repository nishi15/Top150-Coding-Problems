'''
34. Find First and Last Position of Element in Sorted Array
Medium

13514

337

Add to List

Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''

'''
Assumptions i made :-
1. apply binary search first
2. if target found at mid ------ then there are 2 possibilities
        2.1 repeating nums present at left of mid
        2.2 repeating nums present at right of mid
3. need to take both cases in consideration and find min annd max of mid


'''
class Solution:
    def searchRange(self, nums, target: int) :
        
        # initialising left, right and mid pointers
        l =0
        r = len(nums) -1

        while l <= r:
            mid = (l+r)//2

            # if we found the target
            if target == nums[mid]:
                print(mid)
                left_mid = mid
                
                # if the number is in the left side of mid
                while nums[left_mid] == nums[left_mid-1] and left_mid > 0:
                    left_mid -=1

                r_mid = mid
                # if the number is right side of the mid
                while r_mid < r and nums[r_mid] == nums[r_mid+1]:
                    r_mid +=1
 
                # taking the min /max of both left/right side of mid
                left_mid = min(left_mid,mid)                
                r_mid = max(r_mid,mid)

                return [left_mid,r_mid]

            if target <= nums[mid]:
                r =mid -1
            else:
                l = mid+1

        return [-1,-1]

    def searchRange_bettersol(self, nums, target: int) :
        left = self.helper(nums, target,True)
        right = self.helper(nums, target,False)
        return [left,right]

    def helper(self,nums,target,left):
        l = 0
        r = len(nums)-1
        i = -1
        while l <=r:
            mid = (l+r) // 2
            if target == nums[mid]:
                i = mid
                if left:
                    r = mid-1
                else:
                    l = mid+1

            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid+1
        return i


if __name__ == "__main__":
    sol = Solution()
    # print(sol.searchRange(nums = [1,2,3], target = 1))
    print(sol.searchRange_bettersol(nums = [1,2,3], target = 1))