# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 10:19:09 2015

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.


@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        """由于矩阵是sorted.target先跟每行最大的比较确定行，再确定是
        该行的哪一列。Two passes, worse case O(m + n) time."""
        j = len(matrix[0]) - 1
        i = 0
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
    
    def searchMatrix2(self, matrix, target):
        """两次二分查找。O(logm+logn)"""
        m = len(matrix)
        n = len(matrix[0])
        
        L = 0
        R = m - 1
        while L <= R:
            M = (L + R)/2
            if matrix[M][0] == target:
                return True
            elif matrix[M][0] > target:
                R = M - 1
            else:
                L = M + 1
        row = R # this is the row
        
        L = 0
        R = n - 1
        while L <= R:
            M = (L + R)/2
            if matrix[row][M] == target:
                return True
            elif matrix[row][M] > target:
                R = M - 1
            else:
                L = M + 1
        return False
        
        
        
sol = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
matrix2 = [[1]]
print sol.searchMatrix(matrix,3)
print sol.searchMatrix2(matrix2,0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        