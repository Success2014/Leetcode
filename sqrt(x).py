# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 12:25:13 2015

Implement int sqrt(int x).

Compute and return the square root of x.


Assume that x >= 0

@author: Neo
"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0
        i = 1
        j = x/2 + 1
        while i <= j:
            c = (i + j)/2
            if c**2 == x:
                return c
            elif c**2 > x:
                j = c - 1
            else:
                i = c + 1
        return j

sol = Solution()
print sol.mySqrt(100)