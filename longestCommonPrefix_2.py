# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 11:06:46 2015

@author: Neo
"""

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        first = strs[0]
        n = len(first)
        res = ''
        for i in xrange(n):
            for word in strs[1:]:
                if len(word) == i or word[i] != first[i] :
                    return res
            res += first[i]
        return res
            
        
        