# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 14:49:52 2015

Given an integer n, generate a square matrix filled with elements from 1 to 
n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        """思路跟spiral matrix差不多"""
        if n < 1:
            return []
        total = n*n
        each = 1
        m = n # row
#        res=[[0]*n] * n # this is wrong, all referred to the same object
        res = [[0 for i in range(n)] for j in range(n)]
        row = 0
        column = -1
        while True:
            for i in xrange(n):
                column += 1
                res[row][column] = each
                each += 1
            if each > total:
                return res                
            m = m - 1
            
            for j in xrange(m):
                row += 1
                res[row][column] = each
                each += 1
            if each > total:
                return res            
            n = n - 1
            
            for i in xrange(n):
                column -= 1
                res[row][column] = each
                each += 1
            if each > total:
                return res            
            m = m - 1
            
            for j in xrange(m):
                row -= 1
                res[row][column] = each
                each += 1            
            if each > total:
                return res
            n = n - 1
                
                
sol = Solution()
print sol.generateMatrix(1)
                
                