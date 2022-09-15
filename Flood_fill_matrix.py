'''
733. Flood Fill
Easy

5399

523

Add to List

Share
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

'''

class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        rows = len(image)
        cols = len(image[0])
        val = image[sr][sc]
        
        def fill_pixel(image,sr,sc,val,color):

            # checking the bound for rows and col of matrix
            if 0 <= sr < rows and 0<= sc < cols and image[sr][sc] == val:

                # replacing the given value with color
                image[sr][sc] = color
                
                # finding top recursively
                fill_pixel(image,sr-1,sc,val,color)

                # finding bottom recursively
                fill_pixel(image,sr+1,sc,val,color)
                
                # finding left recursively
                fill_pixel(image,sr,sc-1,val,color)

                # finding right recursively
                fill_pixel(image,sr,sc+1,val,color)

            # returning the image
            return image
        
        return fill_pixel(image,sr,sc,val,color)



sol = Solution()
res = sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
print(res)