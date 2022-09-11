'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int):
        output = []

        for i in range(1,numRows+1):
            tmp = []
            for j in range(i):
                if j == 0 or j==i-1:
                    tmp.append(1)
                else:
                    tmp.append(output[i-2][j] + output[i-2][j-1])
            
            output.append(tmp)

        print(output)
     

sol = Solution()
sol.generate(5)