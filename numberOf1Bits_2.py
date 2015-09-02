# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 21:03:16 2015

@author: Neo
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        c = 0
        for i in range(32):
            if n & 1:
                c += 1
            n >>= 1
        return c
    def hammingWeight2(self, n):
        c = 0
        while n:
            n = n & (n-1)
            c += 1
        return c
        