# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:47:23 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
        
        
        