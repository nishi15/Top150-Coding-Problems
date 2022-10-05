'''
300. Longest Increasing Subsequence
Medium

14983

269

Add to List

Share
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''


class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def lengthOfLIS_rcursive(self, nums) -> int:
        return self.solve(nums,0,len(nums),0)

    def solve(self,nums,i,n,prev):
        if n == 0:
            return 0

        exclude = self.solve(nums,i+1,n-1,prev)
        include = 0

        if nums[i] > prev:
            include = 1 + self.solve(nums,i+1,n-1,nums[i])

        return max(include,exclude)


sol = Solution()
res = sol.lengthOfLIS_rcursive([1,2,5])
print(res)