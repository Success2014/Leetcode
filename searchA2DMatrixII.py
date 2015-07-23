# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:27:46 2015

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

Hide Tags Divide and Conquer Binary Search
Hide Similar Problems (M) Search a 2D Matrix




@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        """和上题第一种解法一模一样的代码，但是却有不同的含义。
        这次是先找到对应的列，然后找对应的行。O(m+n) time complexity."""
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
        
        





















