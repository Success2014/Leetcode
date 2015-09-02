# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 11:35:39 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        num_d = {}
        while n != 1 and n not in num_d:
            num_d[n] = 1
            summ = 0
            while n:
                digit = n % 10
                summ += digit*digit
                n = n / 10
            n = summ
        return n == 1