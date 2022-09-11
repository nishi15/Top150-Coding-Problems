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
        dp = [["" for x in range(sum+1)] for y in range(len(arr)+1)]

        for i in range(len(arr)+1):
            for j in range(sum+1):
                if i==0 and j>0:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = 1
                elif arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        print(dp[len(arr)][sum])


    def subset_recursion(self,arr,sum,count):
        if sum == 0:
            count +=1
            return count
        
        if not arr:
            return 0

        itm = arr.pop()
        if itm <= sum:
            return self.subset_recursion(arr,sum-itm,count) + self.subset_recursion(arr,sum,count)
        else:
            return self.subset_recursion(arr,sum,count)   

        


if __name__ == "__main__":
    sol = Solution()
    arr = [2,3,5]
    print(sol.subset(arr,5))
    # print(sol.subset_recursion(arr,10,0))