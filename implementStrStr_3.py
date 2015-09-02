# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:44:59 2015

@author: Neo
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0
            
        for i in xrange(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle):
                    if haystack[i+j] != needle[j]:
                        break
                    j += 1
                
                j -= 1    
                if haystack[i+j] == needle[j] and j == len(needle) - 1:
                    return i
        
        return -1
                    
            
            
            
        
        
        
        
        
        