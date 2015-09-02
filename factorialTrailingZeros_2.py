# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 09:17:50 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        count = 0
        divisor = 5
        while n >= divisor:
            count += n / divisor
            divisor *= 5
        return count