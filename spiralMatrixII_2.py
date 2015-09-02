# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:51:01 2015

@author: Neo
"""


class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        """思路与spiral matrix差不多。"""
        if not n :
            return []
        nrow = n
        ncol = n
        
        
        matrix = [[0 for i in xrange(n)] for j in xrange(n)]
        i = 0
        j = -1
        c = 1
        while True:
            for y in xrange(ncol):
                j += 1
                matrix[i][j] = c
                c += 1
                
            nrow -= 1
            if nrow == 0:
                return matrix
            for x in xrange(nrow):
                i += 1
                matrix[i][j] = c
                c += 1
            
            ncol -= 1
            if ncol == 0:
                return matrix
            for y in xrange(ncol):
                j -= 1
                matrix[i][j] = c
                c += 1
            
            nrow -= 1
            if nrow == 0:
                return matrix
            for x in xrange(nrow):
                i -= 1
                matrix[i][j] = c
                c += 1
            
            ncol -= 1
            if ncol == 0:
                return matrix
            

sol = Solution()                
print sol.generateMatrix(1)
                
                
                
                
                
                
        
        