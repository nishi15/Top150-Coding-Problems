'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


'''

# Explanation :-
# Need to find x + y + z = 0
# We will fix 'x' , and then iterate the list for two sum of y & z
# Will keep iterating for each x combination
# Also if a nuber is already chooses as x , will skip as it will eventualy lead to same pair

class Solution:
    def threeSum(self, nums):
        # sorting the array
        nums.sort()
        res = []
        print(nums)
        for i,val in enumerate(nums):
            print(i)
            # choosing x =  val 
            if i>0 and nums[i-1] == val:
                continue

            # getting left and right pointers for nums - i of array  
            l = i+1 
            r = len(nums) -1
            
            while l <r:
                # calculating sum
                threesum = val + nums[l] + nums[r]

                # Updating left and right pointers accordingly

                if threesum < 0:
                    l = l+1                    
                elif threesum > 0:
                    r = r-1
                else:
                    res.append([val,nums[l],nums[r]])
                    l = l+1

                    # we also need to skip for seen left pointer value to avoid duplicacy.
                    # by seeing ony left we ensure no duplicates present as x,y already been unique, no need to check for z i.e right pointer
                    while nums[l] == nums[l-1] and l<r:
                        l = l+1
        return res


if __name__ == "__main__":
    sol = Solution()
    r  = sol.threeSum([-1,0,1,2,-1,-4])
    print(r)