'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # ------------- Bits appraoch ---------- #
        # Time : O(1)
        # Space : O(1)
        return n> 0 and n & (n-1) == 0

        #--------- Recursive approach --------------- #
        # Time : O(logn)
        # Space : O(logn)
        if n < 0:
            return False
        if n == 1:
            return True
        if n %2 !=0:
            return False
        return self.isPowerOfTwo(n//2)

        # ---------- Iterative approach ---------------- #
        # Time : O(logn)
        # Space : O(1)   
        while n:
            if n == 1:
                return True
            if n%2 == 0:
                n = n//2
            else:
                return False
            
        return True

if __name__ == "__main__":
    sol = Solution()
    res = sol.isPowerOfTwo(6)
    print(res)
        
            