# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 17:19:04 2015

这一排的数，除了开头和结尾，等于上一排的两个数相加

@author: Neo
"""

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result = []
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        result.append([1,1])
        if numRows == 2:
            return result
        
        for n in xrange(2, numRows): # n is the index            
            cur_row = [1 for j in range(n+1)]
            for i in xrange(n + 1):
                if i != 0 and i != n:
                    cur_row[i] = result[n-1][i-1] + result[n-1][i]
            result.append(cur_row)
        
        return result
                
                
sol = Solution()        
print sol.generate(4)
        
        
        
        