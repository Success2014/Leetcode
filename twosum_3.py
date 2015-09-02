# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:40:46 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = {}
        for idx,val in enumerate(nums):
            if d.has_key(target - val):
                return (d[target - val]+1,idx+1)
            else:
                d[val] = idx
        
        
        
        
        
        