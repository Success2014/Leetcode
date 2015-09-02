# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 10:45:00 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        L = 0
        R = len(nums) - 1
        while L < R:
            M = (L + R) / 2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]