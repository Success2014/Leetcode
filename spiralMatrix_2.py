# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:58:05 2015

@author: Neo
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0]) + 1#方便第23行代码
        if n == 1:
            return []
        
        res = []
        i = 0
        j = -1
        while m>0 and n>0:
            n -= 1
            if m>0 and n>0:
                for x in xrange(n):
                    j += 1
                    res.append(matrix[i][j])
                
            m -= 1
            if m>0 and n>0:
                for y in xrange(m):
                    i += 1
                    res.append(matrix[i][j])
                    
            n -= 1
            if m>0 and n>0:
                for x in xrange(n):
                    j -= 1
                    res.append(matrix[i][j])
            
            m -= 1
            if m>0 and n>0:
                for y in xrange(m):
                    i -= 1
                    res.append(matrix[i][j])
        
        return res
                
                    
        