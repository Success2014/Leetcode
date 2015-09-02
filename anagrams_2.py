# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 16:30:11 2015

@author: Neo
"""

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        res = []
        d = {}
        for word in strs:
            word_st = ''.join(sorted(word))
            if word_st in d:
                d[word_st].append(word)
            else:
                d[word_st] = [word]
        
        for idx, val in d.items():
            if len(val) > 1:
                res += val
        
        return res
        



sol = Solution()        
strs = ["",""]
print sol.anagrams(strs)