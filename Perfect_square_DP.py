'''
279. Perfect Squares
Medium

7487

320

Add to List

Share
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

'''


'''
1. we will use BFS algorithm here to get the ans
2. for each level in our tree , we will loop to ith squares'
3. after looping each level we will in depth


'''

class Solution:
    def numSquares(self, n):
        # perfetc squares less than n
        squares = [i**2 for i in range(1,int(n**0.5)+1)]

        # root node
        currentlevel = {n}
        levels = set()
        level_depth = 1
        
        # Looping through each level of BFS
        while currentlevel:

            # Lopping through each node of givn level from left -> right
            for node in currentlevel:

                # each perfetc square supported in each level
                for sq in squares:


                    if node == sq:
                        return level_depth
                    if node < sq:
                        break
                    levels.add(node-sq)

            # updating current level to new level   
            currentlevel = levels

            # re-intialising the level
            levels = set()

            # incrementing depth as we have visited one level from left -> right
            level_depth +=1
            
        return n




sol = Solution()
res  = sol.numSquares(12)
print(res)