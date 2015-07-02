# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 13:32:07 2015

Given a matrix of m x n elements (m rows, n columns), return all 
elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].


@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):        
        """沿着矩阵向右n步，向下m-1步，向左n-1步，向上m-2步...
        直到m或者n为0停止"""
        res = []
        m = len(matrix) # rows of matrix
        if m == 0:
            return res
        n = len(matrix[0]) # columns of matrix
        
        row = 0 # current row index
        column = -1 # current column index
        while True:
            
            for i in xrange(n): # walk right
                column += 1
                res.append(matrix[row][column])                
            
            m = m - 1            
            if m == 0:
                return res
                
            for j in xrange(m): # walk down
                row += 1
                res.append(matrix[row][column])
            
            n = n - 1
            if n == 0:
                return res
                
            for i in xrange(n): # walk left
                column -= 1
                res.append(matrix[row][column])
            
            m = m - 1
            if m == 0:
                return res                
            
            for j in xrange(m): # walk up
                row -= 1
                res.append(matrix[row][column])
            
            n = n - 1
            if n == 0:
                return res


sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix2 = [[3],[2]]
matrix3 = []
print sol.spiralOrder(matrix3)