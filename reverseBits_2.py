# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 11:26:59 2015

@author: Neo
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans
    
    def reverseBits2(self, n):
        map_table = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
        ans = 0
        for i in xrange(8):
            ans <<= 4
            curt = n & 15
            ans |= map_table[curt]
            n >>= 4
        return ans
            
            
            
            
            