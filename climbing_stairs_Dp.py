'''
70. Climbing Stairs
Easy

13951

411

Add to List

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''

class Solution:
    def climbStairs(self, n: int) -> int:       
        
        t = [-1]*(n+1)
        
        res = self.climb(n,t)
        return res
        
    def climb(self,n,t):
        print(t)
        if n==1:
            t[n] = 1
            return t[n]
        if n == 2:
            t[n] = 2
            return t[n]
        if t[n] != -1:
            return t[n]
        else:
            t[n] = self.climb(n-1,t) + self.climb(n-2,t)
            return t[n]

    def climbRecursion(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        s = self.climbRecursion(n-1) + self.climbRecursion(n-2)
        return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbRecursion(4))
    print("-"*20)
    print(sol.climbStairs(4))