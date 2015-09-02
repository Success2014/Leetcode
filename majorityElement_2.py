# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 16:18:51 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        d = {}
        n = len(nums)
        for num in nums:
            if num in d:
                d[num] += 1
                if d[num] > n / 2:
                    return num
            else:
                d[num] = 1
                if d[num] > n / 2:
                    return num
        
        
        
        