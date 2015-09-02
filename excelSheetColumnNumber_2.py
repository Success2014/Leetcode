# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 00:25:08 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        res = 0
        power = 0
        for i in xrange(len(s)-1,-1,-1):
            res += (ord(s[i]) - ord('A') + 1) * (26**power)
            power += 1
        
        return res
        