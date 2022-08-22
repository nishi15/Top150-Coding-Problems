'''
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

class Solution:
    def maxArea(self, height) -> int:
        
        # naive approach - O(n2)
        # making each possible pair of heights to get max_area
        '''
        max_water =0
        for i in range(len(height)):
            for j in range(len(height)):
                if i == j :
                    continue
                length = min(height[i],height[j])
                width = abs(i-j)
                max_water = max(length*width,max_water)
                
        return max_water
        '''

        # better approach 
    
        max_water = 0

        #taking the maximum width
        l ,r = 0,len(height) - 1

        while l <r:
            length = min(height[l],height[r])
            width = r -l 
            area = length * width
            max_water = max(max_water,area)

            # if l < r -> update left pointer
            # else update right pointer
            if height[l] < height[r]:
                l +=1
            else:
                r -=1

        return max_water
                    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,1]))