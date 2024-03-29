'''
342. Power of Four
Easy

2575

314

Add to List

Share
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        print(bin(n))
        if n ==1:
            return True
        return n >0 and n & (n-1) == 0 
        

sol = Solution()
print(sol.isPowerOfFour(8))