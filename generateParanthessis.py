'''
22. Generate Parentheses
Medium

14907

562

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''

class Solution:
    def generateParenthesis(self, n):
        if not n :
            return  []

        left,right,res = n,0,[]
        self.dfs(left,right,res,"")
        return res

    def dfs(self,left,right,res,s):
        if not left and not right:
            res.append(s)
            return 

        if left:
           self.dfs(left-1,right+1,res,s+"(")

        if right:
            self.dfs(left,right-1,res,s+")")


            

sol = Solution()
print(sol.generateParenthesis(2))