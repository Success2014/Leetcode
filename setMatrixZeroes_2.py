# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:54:21 2015

@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        firstRow = False
        firstCol = False
        
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRow = True
                    if j == 0:
                        firstCol = True
                    
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRow:
            for j in xrange(n):
                matrix[0][j] = 0
        if firstCol:
            for i in xrange(m):
                matrix[i][0] = 0
        
                
        
        
        
        
        