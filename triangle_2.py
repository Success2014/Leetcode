# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:30:18 2015

@author: Neo
"""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        res = [0 for i in xrange(n)]
        res[0] = triangle[0][0]
        for i in xrange(1,n):
            for j in xrange(i,-1,-1):
                if j == i:
                    res[j] = res[j-1] + triangle[i][j]
                elif j == 0:
                    res[j] +=  triangle[i][j]
                else:
                    res[j] = min(res[j],res[j-1]) + triangle[i][j]
                    
        return min(res)
        
        
        
        