# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:23:48 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
        return True
        
        
        