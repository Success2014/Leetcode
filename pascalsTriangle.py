# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 17:19:04 2015

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Tags Array
Similar Problems (E) Pascal's Triangle II



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
    
    def generate2(self, numRows):
        """idea一样，但是更简洁"""
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
                
                
sol = Solution()        
print sol.generate(8)
        
        
        
        