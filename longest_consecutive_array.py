'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''

class Solution:
    def longestConsecutive(self, nums):
        nums = sorted(nums)
        current_streak = 1
        longest_streak = 1

        for i in range(1,len(nums)):
            # print(nums[i]-nums[i-1])
            diff = nums[i]-nums[i-1]
            if diff == 1:
                current_streak+=1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)
    
    def longestConsecutive_optimal(self, nums):
        unique_numbers = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in unique_numbers:
                length = 0

                while (n+length) in nums:
                    length +=1

                longest = max(longest,length)
        
        return longest



if __name__ == "__main__":
    sol = Solution()
    # res = sol.longestConsecutive([100,4,200,1,3,2])
    res = sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
    print(res)
    res = sol.longestConsecutive_optimal([9,1,4,7,3,-1,0,5,8,-1,6])
    print(res)