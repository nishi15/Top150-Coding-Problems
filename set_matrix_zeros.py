'''
Examples 1:

Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

'''

class Solution:
    def __init__(self) -> None:
        pass

    # bruteforce way
    def set_zeros(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    ind = 0
                    # changing all rows
                    while ind <= len(arr[i])-1:
                        if arr[i][ind] != 0:
                            arr[i][ind] = -1
                        ind +=1

                    indj = 0
                    # changing all columns
                    while indj <= len(arr)-1:
                        if arr[indj][j] != 0:
                            arr[indj][j] = -1
                        indj +=1
                        

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == -1:
                    arr[i][j] = 0
        
        return arr

    # better code
    def better_set_zeros(self,arr):
        rows ,cols = len(arr),len(arr[0])
        rowsN = [1]*rows
        colsM = [1]*cols

        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 0:
                    rowsN[i] = 0
                    colsM[j] = 0

        for r in range(len(rowsN)):
            if rowsN[r] == 0:
                for c in range(cols):
                    arr[r][c] = 0

        for c in range(len(colsM)):
            if colsM[c] == 0:
                for r in range(rows):
                    arr[r][c] = 0
        
        return arr


if __name__ == "__main__":
    sol = Solution()
    # res = sol.set_zeros([[1,1,1],[1,0,1]])
    res = sol.better_set_zeros([[1,0,1],[1,0,1]])
    print(res)