# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 00:16:59 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        res = ''
        while n:
            res = chr(ord('A') + (n - 1)%26) + res
            n = (n - 1) / 26
        return res