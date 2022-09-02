'''
54. Spiral Matrix
Medium

8640

902

Add to List

Share
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

'''

class Solution:
    def spiralOrder(self, matrix):
        top = left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) -1
        res=[]
        
        while True:
            if not (left <= right and top <= bottom):
                break
            
            # right -> left : top row
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top +=1
            
            # top -> bottom : right col
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -=1
            
            
            
            # right -> left : bottom row
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom -=1
            
            # bottom -> top : left col
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left +=1
        
        return res    

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[2,5,8],[4,0,-1]]))