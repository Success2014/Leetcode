# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:24:56 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        p0 = 0
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[p0],nums[i] = nums[i],nums[p0]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i],nums[p2] = nums[p2],nums[i]
                p2 -= 1
            else:
                i += 1
            
        
        
        
        
        