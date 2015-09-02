# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:03:17 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if not s:
            return True
        d = {')':'(','}':'{',']':'['}
        stack = []
        
        for p in s:
            if not d.has_key(p):
                stack.append(p)
            else:
                if not stack:
                    return False
                else:
                    tmp = stack.pop()
                    if tmp != d[p]:
                        return False
        
        return len(stack) == 0
        
        
        
        