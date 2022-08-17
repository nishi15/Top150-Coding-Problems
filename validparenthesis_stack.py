'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        paran_dict = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        for c in s:            
            if c in paran_dict:
                if stack and stack[-1] == paran_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True

        return False




if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("[()]"))