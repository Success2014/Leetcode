# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 17:24:25 2015

@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for i in xrange(m):
            for j in xrange(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in xrange(m):
            for j in xrange(0,n/2):
                matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
        
        
        
        