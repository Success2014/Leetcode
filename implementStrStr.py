# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:32:18 2015

Implement strStr().

Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.


@author: Neo
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}

    """brute force, two pointers"""
    def strStr(self, haystack, needle):
        
        lenH = len(haystack)
        lenN = len(needle)
        
        if lenH < lenN:
            return -1
        
        for i in xrange(lenH - lenN + 1): # first pointer i, for haystack
            
            j = 0 # second pointer j, for needle
            k = i # temporary pointer, to loop in haystack
            
            while j < lenN:
                if needle[j] == haystack[k]:
                    j += 1
                    k += 1
                else:
                    break
            
            if j == lenN:
                return i 
                
        
        return -1
            

sol = Solution()
print sol.strStr("abcdef","ef")










