'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        '''
        m.logn
        '''
        i = 0

        while i < len(matrix):

            left = 0
            right = len(matrix[i]) - 1
            data = matrix[i]
            while left <= right:
                mid = (left + right) //2

                if data[mid] < target:
                    left = mid+1
                elif data[mid] > target:
                    right = right -1
                else:
                    print(data[mid])
                    return True
            i =i+1
        
        return False
                

            

if __name__  == "__main__":
    sol = Solution()
    res = sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
    print(res)