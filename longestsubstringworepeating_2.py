# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 11:55:43 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        res = 0
        cur = 0
        d = {}
        for i,c in enumerate(s):
            if c not in d:
                cur += 1
            else:
                cur = min(cur + 1, i - d[c])
            d[c] = i
            res = max(res, cur)
        return res
                
            
        
        
        
        
            
        
sol = Solution()
s1 = "cdd"
s2 = "bdb"
s3 = "aaaa"
s4 = "tmmzuxt"
print sol.lengthOfLongestSubstring(s4)
        
        