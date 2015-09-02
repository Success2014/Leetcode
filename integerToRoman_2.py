# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 11:04:36 2015

@author: Neo
"""

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 
                  100, 90, 50, 40,
                  10, 9 , 5, 4,
                  1]
        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV",
                   "I"]
        res = ""
        while num > 0:
            for idx, val in enumerate(values):
                div = num / val
                for i in xrange(div):
                    res += symbols[idx]
                    num -= val
        return res