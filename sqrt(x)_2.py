# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:26:27 2015

@author: Neo
"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if not x:
            return 0
        L = 1
        R = x / 2 + 1
        while L <= R:
            M = (L + R) / 2
            if M*M == x:
                return M
            elif M*M > x:
                R = M - 1
            else:
                L = M + 1
        
        return R
        
        
sol = Solution()        
print sol.mySqrt(8)
print sol.mySqrt(10)
print sol.mySqrt(125)