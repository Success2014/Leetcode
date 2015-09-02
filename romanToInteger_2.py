# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 11:15:07 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman_dict = {'I' : 1,
                  'V' : 5,
                  'X' : 10,
                  'L' : 50,
                  'C' : 100,
                  'D' : 500,
                  'M' : 1000}
        prev = 0
        curr = 0
        res = 0
        for letter in s:
            curr = roman_dict[letter]
            if curr > prev:
                res += curr - 2 * prev
            else:
                res += curr
            prev = curr
        return res