'''
62. Unique Paths
Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

'''

'''
Approach followed :-
1. set two variables right and down as 0 ,0
2. make a choice diagram by exhauting eachi right and down path taken
    a. The base condition for choice tree will be :
        > when we reach to the rightmost path i.e right >= n
        > when we reach to the bottom of matrix i.e down >= m

    b. recursively check the base condition
    c. add up both paths to get final count


'''

class Solution:

    def uniquePaths_Recursion(self, m: int, n: int) -> int:
        
        # right and down pointers
        r =d =0

        # if we are already at source
        if m ==1 and n ==1:
            return 1
        
        return self.solve1(m,n,r,d)


    def solve1(self,m,n,r,d):

        # base condition of reaching rightmost and bottom of the given matrix bounds
        if r >=n or d >=m:
            return 0


        # choosing right path recursively
        right = self.solve(m,n,r+1,d)

        # choosing down path recursively
        down = self.solve(m,n,r,d+1)

        # if we reached to the end of array after recursive traversing
        if r == n-1 and d == m-1:
            return 1

        # adding up both right and down paths taken so far
        return right+down

    def uniquePaths_memoization(self, m: int, n: int) -> int:
        '''
        Since recursive is extensive solution we use some extra bit of space to store all the possible seen paths into the matrix of size mxn
         
        Use these stored values if we encounter same possible set again.

        '''
        r =d =0
        if m ==1 and n ==1:
            return 1
        
        # initialising the matrix
        mat = [[0 for i in range(n)] for j in range(m)]
        self.solve(m,n,r,d,mat)
        return mat[0][0]
    
    def solve(self,m,n,r,d,mat):
        if r >=n or d >=m:
            return 0

        if mat[d][r]:
            return mat[d][r]

        right = self.solve(m,n,r+1,d,mat)
        down = self.solve(m,n,r,d+1,mat)

        if r == n-1 and d == m-1:
            return 1
        
        # saving the result to the matrix
        mat[d][r] = right+down
        return mat[d][r]



sol = Solution()
res = sol.uniquePaths_memoization(1,1)
print(res)