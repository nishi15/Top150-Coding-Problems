'''
131. Palindrome Partitioning
Medium

8254

249

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''

'''
Solution :-

1. this is a backtracking problem -> general all decompositin of the string and see which are palindromes
2. we will divide the string in k parts ,
3. k will be moving exhautively to the length f string to find out all decomposition 
4. if the part is palindrome , add it to temp list and serch for rest of the string

'''

class Solution:
    def partition(self, s):
        res = []
        temp = []
        # calling helper function
        self.solve(s,0,temp,res)
        return res


    def solve(self,s,idx,temp,res):

        # Base condition :- when idx == len(s)
        if idx == len(s):
            res.append(temp[::-1])
            return

        # looping to each decomposition of s
        for k in range(idx+1,len(s)+1):
            print(s[idx:k])

            # getting the prefix part
            prefix = s[idx:k]

            # if it is palindrome , then search for rest of the string
            if prefix == prefix[::-1]:
                self.solve(s,k,[prefix] + temp,res)       

        


sol = Solution()
print(sol.partition("aab"))
    