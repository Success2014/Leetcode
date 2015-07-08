# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 10:24:18 2015

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?


解题思路：先将矩阵转置，然后将矩阵的每一行翻转，就可以得到所要求的矩阵了。
1 2 3
4 5 6
7 8 9

1 4 7
2 5 8
3 6 9

7 4 1
8 5 2
9 6 3


@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in xrange(n):
            matrix[i].reverse()
        
        return matrix
    
    def rotate2(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in xrange(n):
            for j in xrange(n/2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
        
        return matrix


sol = Solution()        
print sol.rotate2([[1,2,3],[4,5,6],[7,8,9]])
        
        
        
        
        
        
        
        
        
        
        
        
        
        