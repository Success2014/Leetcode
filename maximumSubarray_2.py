# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 21:36:26 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        maxSoFar = nums[0]
        maxEndHere = nums[0]
        
        for num in nums[1:]:
            maxEndHere = max(num, num+maxEndHere)
            maxSoFar = max(maxEndHere, maxSoFar)
        return maxSoFar
        