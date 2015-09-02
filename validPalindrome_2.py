# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:54:00 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if not s:
            return True
        L = 0
        R = len(s) - 1
        while L < R:
            if s[L].isalnum() and s[R].isalnum():
                if s[L].lower() == s[R].lower():
                    L += 1
                    R -= 1
                else:
                    return False
            else:
                if not s[L].isalnum():
                    L += 1
                else:
                    R -= 1
        return True
            
            
        