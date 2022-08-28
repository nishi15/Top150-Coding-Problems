'''
 
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.

'''

class Solution:

    def subset(self,arr,sum):
        dp = [[0 for x in range(sum+1)] for y in range(len(arr)+1)]
        n = len(arr)

        for i in range(n+1):
            for j in range(sum+1):
                if j>0 and i==0:
                    dp[i][j] = False                   
                
                elif j == 0:
                    dp[i][j] = True                
              
                elif arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        print(dp)
    
        return dp[n][sum]
        


if __name__ == "__main__":
    sol = Solution()
    arr = [2,3,7,8,10]
    print(sol.subset(arr,6))