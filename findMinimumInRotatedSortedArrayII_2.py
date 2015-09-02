# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 10:56:05 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        L = 0
        R = len(nums) - 1
        while L < R and nums[L] >= nums[R]:
            M = (L + R)/2
            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[R]:
                R = M
            else:
                L += 1
        return nums[L]