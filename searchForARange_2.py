# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:20:58 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        L = self.fLeft(nums, target)
        R = self.fRight(nums, target)
        return [L,R]
    
    def fLeft(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        
        if L < len(nums) and nums[L] == target:
            return L
        else:
            return -1
    
    def fRight(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] > target:
                R = M - 1
            else:
                L = M + 1
        
        if R < len(nums) and nums[R] == target:
            return R
        else:
            return -1
        
        
        
        
        
        