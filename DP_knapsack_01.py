'''
Knapsack [0/1] 

Knapsack Max weight       :       W = 10 (units)

Total items              :       N = 4

Values of items          :       v[] = {10, 40, 30, 50}

Weight of items          :       w[] = {5, 4, 6, 3}

The goal is maximise the profit
'''

global recursive_calls,memoization_calls
recursive_calls = 0 
memoization_calls = 0

def knapsack(price,weight,W,n):
    global recursive_calls
    recursive_calls +=1
    
    if (n== 0) or W == 0:
        return 0

    ind = n-1

    # print(f"Calling for {ind}")
    # print("Parameters , ",price,weight,W,n)

    # if item weight is less thand and equal to Knapsack Weight ---> 2 Choices : (Accept,Reject)
    if weight[ind] <= W:
        # print("-"*20)
        # print(price[ind])
        # print(weight[ind])        
        # print("-"*20)
        return max((price[ind] + knapsack(price[:ind],weight[:ind],W-weight[ind],n-1)),(knapsack(price[:ind],weight[:ind],W,n-1)))
        pass

    # if item weight is greater than Knapsack weight --> reject
    return knapsack(price[:ind],weight[:ind],W,n-1)


def knapsack_memo(price,weight,W,n):
    mat = []
    for i in range(n+1):
        mat.append([-1 for j in range(W+1)])

    return __knapsack_memoization(price,weight,W,n,mat)


def __knapsack_memoization(price,weight,W,n,mat):
    
    global memoization_calls
    memoization_calls +=1

    if n==0  or W==0:
        return 0

    if mat[n][W] != -1:
        return mat[n][W]

    ind = n-1

    if weight[ind] <= W:
        mat[n][W] = max((price[ind]+ __knapsack_memoization(price[:ind],weight[:ind],W-weight[ind],n-1,mat)),__knapsack_memoization(price[:ind],weight[:ind],W,n-1,mat))
        return mat[n][W] 

    else:
        mat[n][W] = __knapsack_memoization(price[:ind],weight[:ind],W,n-1,mat)
        return mat[n][W]

    
def knapsack_dp(price,weight,W,n):
    
    #initialisation with base condn (0)
    mat = [["" for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n+1):
        for j in range(W+1):
            if i ==0 or j==0:
                mat[i][j] =0

            elif weight[i-1] <= j:
                mat[i][j] = max((price[i-1] + mat[i-1][j-weight[i-1]]),mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]
    
    return mat[n][W]   

profit = knapsack(price=[10, 40, 30, 50],weight=[5, 4, 6, 3],W=10,n=4)
print(f'Recursion calls {recursive_calls} and result = {profit}')

profit = knapsack_memo(price=[10, 40, 30, 50],weight=[5, 4, 6, 3],W=10,n=4)
print(f'Memoization calls {memoization_calls} and result = {profit}')

profit = knapsack_dp(price=[10, 40, 30, 50],weight=[5, 4, 6, 3],W=10,n=4)
print(f'Dp result = {profit}')