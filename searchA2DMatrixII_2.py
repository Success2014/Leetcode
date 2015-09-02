# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 01:09:12 2015

@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n - 1
        
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        
        return False
        
        
        