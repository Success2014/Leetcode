# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:22:04 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        i = 0
        j = 0
        
        while j < len(nums):
            if j == len(nums) - 1 or nums[j+1] - nums[j] != 1:
                if j > i:
                    res.append("{0}->{1}".format(nums[i],nums[j]))
                else:
                    res.append(str(nums[i]))
            
                i = j + 1
            j += 1
        
        return res
        

sol = Solution()        
print sol.summaryRanges([0,1,2,4,5,7])    
print sol.summaryRanges([0,1,2,3,5,7,9,10])