# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 00:48:19 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        d = {}
        for i in xrange(l1):
            if d.has_key(s[i]):
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            
            if d.has_key(t[i]):
                d[t[i]] -= 1
            else:
                d[t[i]] = -1
                
        for val in d.values():
            if val != 0:
                return False
        
        return True
        
        
s = "a"
t = "a"
sol = Solution()
print sol.isAnagram(s,t)