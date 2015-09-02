# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 09:57:17 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]
        res = []
        for i in xrange(len(nums)):
            for num in self.permute(nums[i+1:]+nums[:i]):
                res.append([nums[i]]+num)
        return res
    
            
            
        
    
            
nums = [1,2,3]            
sol = Solution()
print sol.permute(nums)
        