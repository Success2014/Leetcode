# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:01:35 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        return L
        
        
        
        