# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 17:02:35 2015

@author: Neo
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        lenH = len(haystack)
        lenN = len(needle)
        
        if lenH < lenN:
            return -1        
        
        if not needle:
            return 0
        
        for i in xrange(lenH-lenN+1):
            for j in xrange(lenN):
                if haystack[i+j] != needle[j]:
                    break
            if haystack[i+j] == needle[j]:
                return i
        
        return -1
        


haystack = "mississippi"
needle1 = "issipi"        
needle2 = "pi"
sol = Solution()
#print sol.strStr(haystack,needle1)
print sol.strStr(haystack,needle2)