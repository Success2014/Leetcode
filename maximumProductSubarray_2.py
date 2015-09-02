# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 21:16:30 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        maxEndHere = nums[0]
        minEndHere = nums[0]
        maxSoFar = nums[0]
        
        for num in nums[1:]:
            t1 = maxEndHere*num
            t2 = minEndHere*num
            maxEndHere = max(t1,t2,num)
            minEndHere = min(t1,t2,num)
            if maxEndHere > maxSoFar:
                maxSoFar = maxEndHere
        
        return maxSoFar


sol = Solution()        
print sol.maxProduct([-4,-3,-2])