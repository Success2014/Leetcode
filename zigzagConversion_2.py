# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 10:46:52 2015

@author: Neo
"""



class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        tmp = ["" for i in xrange(numRows)]
        direction = 1
        idx = -1
        for i in xrange(len(s)):
            idx += direction
            tmp[idx] += s[i]
            if idx == numRows - 1:
                direction = -1
            elif idx == 0:
                direction = 1
        
        return ''.join(tmp)
        
a1 = "PAYPALISHIRING"
a2 = "ABCDE"
sol = Solution()
print "result is :", sol.convert(a2, 2)
      
        
        