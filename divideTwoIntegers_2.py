# -*- coding: utf-8 -*-
"""
Created on Sun Aug 02 17:38:58 2015

@author: Neo
"""

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        
        dd = abs(dividend)
        dv = abs(divisor)
        
        remain = dd
        total = 0
        
        while remain >= dv:
            tmp = dv
            count = 1
            while tmp+tmp < remain:
                tmp += tmp
                count += count
            
            remain -= tmp
            total += count
            
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            if total >= 2147483648: # if overflows
                return 2147483647
            return total
        else:
            if total >= 2147483648: # if overflows
                return -2147483648
            return 0 - total
        
        
        