# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 19:47:04 2015

@author: Neo
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        n = len(nums)
        if n == 0:
            return 0
        
        i = 0
        while i < len(nums) and nums[i] == val:
            i += 1
        
        if i < len(nums):
            j = 0
        else:
            j = -1
            
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        return j
        
        
        
        

nums = [2]
val = 3
sol = Solution()
print sol.removeElement(nums,val)