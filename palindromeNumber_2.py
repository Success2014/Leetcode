# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 12:52:01 2015

@author: Neo
"""

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x / div:
            div *= 10
        div /= 10
        
        while x:
            if x/div != x%10:
                return False
            x = (x % div) / 10
            div /= 100
        return True