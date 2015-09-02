# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:58:20 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            M = (L + R) / 2
            if nums[M] == target:
                return M
            elif nums[M] >= nums[L]:
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
        return -1
    