# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 16:03:20 2015

@author: Neo
"""

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        res = []
        for i in xrange(numRows):
            cur = []
            for j in xrange(i+1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(res[i-1][j-1]+res[i-1][j])
            res.append(cur)
                    
        return res
            
            
            
            