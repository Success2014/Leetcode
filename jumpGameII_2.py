# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 17:29:42 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        res = 0
        cur = 0
        nxt = 0
        
        for i in xrange(len(nums)):
            if i > cur:
                res += 1
                cur = nxt
            nxt = max(nxt, i + nums[i])
            
            if cur >= len(nums) - 1:
                return res