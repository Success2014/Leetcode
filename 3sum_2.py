# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:59:42 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        for i in xrange(n):
            if i == 0 or nums[i-1] != nums[i]:
                left = i + 1
                right = n - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        res.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < n and nums[left] == nums[left-1]:
                            left += 1
                        while right > -1 and nums[right] == nums[right+1]:
                            right -= 1
                    elif s < 0:
                        left += 1
                    else:
                        right -= 1
            
        return res
            
            
            
            
            