# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 12:56:39 2015

Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        """O(m + n) space solution"""
        m = len(matrix)
        n = len(matrix[0])
        row = [False for i in range(m)]
        col = [False for j in range(n)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in xrange(m):
            for j in xrange(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
                    
        return matrix
    
    def setZeroes2(self, matrix):
        """constant space solution. Record where the 0s are to the first row
        and first column. Before doing that record whether first row or first
        column has zero."""
        m = len(matrix)
        n = len(matrix[0])
        firstrow = False
        firstcol = False
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    # Check whether the first row and column contain
                    # zeroes before recording
                    if i == 0:
                        firstrow = True
                    if j == 0:
                        firstcol = True
                    
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Set zeroes except for the first row and column
#        for i in xrange(1,m):
#            if matrix[i][0] == 0:
#                for j in xrange(1,n):
#                    matrix[i][j] = 0
#        for j in xrange(1,n):
#            if matrix[0][j] == 0:
#                for i in xrange(1,m):
#                    matrix[i][j] = 0
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstrow:
            for j in xrange(n):
                matrix[0][j] = 0
        if firstcol:
            for i in xrange(m):
                matrix[i][0] = 0
        
        return matrix
        
    



sol = Solution()
print sol.setZeroes([[0,12,3],[24,5,9],[4,523,4]])
print sol.setZeroes2([[0,12,3],[24,5,9],[4,523,4]])