# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:12:49 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = {}
        for idx,num in enumerate(nums):
            if d.has_key(target - num):
                return (d[target-num]+1, idx+1)
            else:
                d[num] = idx
        
        
                
        
        
        