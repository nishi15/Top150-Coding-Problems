'''
5. Longest Palindromic Substring
Medium

21191

1221

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        # res=""

        for i in range(len(s)):

            # for odd occurencs
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > reslen:                    
                    reslen = r-l+1
                    res_l = l
                    res_r = r
                l -=1
                r +=1
            
            # for even occurences
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > reslen:                    
                    reslen = r-l+1
                    res_l = l
                    res_r = r
                r +=1
                l -=1
                

        return s[res_l:res_r+1]

sol =Solution()
print(sol.longestPalindrome("cbbda"))
            
            
            