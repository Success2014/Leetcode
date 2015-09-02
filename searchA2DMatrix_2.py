# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:59:41 2015

@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        # find row
        L = 0
        R = m - 1
        while L <= R:
            M = (L + R) / 2
            if matrix[M][0] == target:
                return True
            if matrix[M][0] > target:
                R = M - 1
            else:
                L = M + 1
        row = R
        
        # find column
        L = 0
        R = n - 1
        while L <= R:
            M = (L + R) / 2
            if matrix[row][M] == target:
                return True
                
            if matrix[row][M] > target:
                R = M - 1
            else:
                L = M + 1
        
        return False
                
                
                
matrix = [[1]]
sol = Solution()
print sol.searchMatrix(matrix,0)