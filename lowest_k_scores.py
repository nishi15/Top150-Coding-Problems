'''
1984. Minimum Difference Between Highest and Lowest of K Scores
Easy

You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

 

Example 1:

Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
Example 2:

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.

'''

# Solution
'''
1. this problem can be solved using sliding window
2. One catch is you can sort the array (to get the diff as close as possible)

'''

class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        
        # taking min from highest limit
        min_diff = 10**6
        
        # sorting the array
        nums.sort()

        # two pointers for sliding window
        l,r=0,k-1
        
        while r < len(nums):
            diff = nums[r]-nums[l]
            print(diff)
            min_diff = min(min_diff,diff)
            l +=1
            r +=1

        return min_diff