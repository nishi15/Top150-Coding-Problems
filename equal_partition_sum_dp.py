'''

Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is the same. 

Examples: 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.

'''


class Solution:

    def subestsum(self,arr,sum,n):
        
        # initialising the matrix
        dp = [[0 for x in range(sum+1)] for y in range(n+1)]

        for i in range(n+1):
            for j in range(sum+1):

                if i==0 and j>0:
                    dp[i][j] = False
                elif j == 0:
                    dp[i][j] = True

                elif arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][sum]

    def equalPartiton(self,arr):
        ar_sum = sum(arr)

        # if the sum of array is odd, it is not possible to have equal sum for any partition
        if ar_sum %2 != 0:
            return False
        else:
            # sum is even,then finding one partition will suffice.
            sum1 = sum2 = ar_sum //2
            return self.subestsum(arr,sum1,len(arr))
            

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 5, 0, 5]
    print(sol.equalPartiton(arr))