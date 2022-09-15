'''
2373. Largest Local Values in a Matrix
Easy

230

23

Add to List

Share
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

 

Example 1:


Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
Example 2:


Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
 

Constraints:

n == grid.length == grid[i].length
3 <= n <= 100
1 <= grid[i][j] <= 100

'''

class Solution:
    def max_neighbor(self,i,j,rows,cols,grid):
        # getting the local aximum from all neighbours
        max_num = 0
        for r in range(i-1,i+2):
            for c in range(j-1,j+2):
                if (i==rows or j==cols or i<0 or j<0):
                    continue
                else:
                    print(r,c)
                    max_num = max(max_num,grid[r][c])
        
        return max_num

    def largestLocal(self, grid):
        rows = cols =len(grid)
        r = c = rows-2
        output = [[0 for j in range(c)] for i in range(r)]
        n=m=0
        for i in range(1,rows):
            if n >=r:
                break            
            for j in range(1,cols):
                if m >= c:
                    break
                output[n][m] = self.max_neighbor(i,j,rows,cols,grid) #grid[i][j]
                m+=1
                print(output)
            m = 0
            n+=1
        
        print(output)


sol = Solution()
sol.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])