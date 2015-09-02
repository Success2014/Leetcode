# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 14:07:51 2015

@author: Neo
"""

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0/self.myPow(x,-n)
        if n % 2:
            return self.myPow(x*x,n/2)*x
        else:
            return self.myPow(x*x,n/2)
        