# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 15:01:21 2015

@author: Neo
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        n = len(s)
        i = 0
        
        res = []
        while i < n and s[i] == " ":#ignore leading spaces
            i += 1
        
        j = i
        while j < n:
            while j < n and s[j] != " ":#track letters
                j += 1
            res.insert(0, s[i:j])
            while j < n and s[j] == " ": #ignore trailing spaces
                j += 1
            i = j
        return ' '.join(res)
        
        
        
        
        
        
s = "a"
sol = Solution()        
print sol.reverseWords(s)