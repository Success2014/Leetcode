# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 11:37:58 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s:
            return ""
        start = 0
        end = 0
        for i in xrange(len(s)):
            len1 = self.expand(i,i,s)
            len2 = self.expand(i,i+1,s)
            lenM = max(len1,len2)
            if lenM > end - start + 1:
                start = i - (lenM - 1) / 2 
                end = i + lenM / 2
        return s[start:end+1]
    
    
    def expand(self, left, right, s):
        while left>=0 and right <len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left -1
        