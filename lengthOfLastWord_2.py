# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 10:08:52 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        n = len(s)
        if n == 0:
            return 0
        
        i = n - 1
        while i >=0 and s[i] == " ":
            i -= 1
        
        j = i
        while j >= 0 and s[j] != " ":
            j -= 1
            
        return i - j