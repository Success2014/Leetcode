# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:26:01 2015

Given an array of integers and an integer k, find out whether there there are 
two distinct indices i and j in the array such that nums[i] = nums[j] and 
the difference between i and j is at most k.

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        nums_dict = {}
        for index, num in enumerate(nums):
            if nums_dict.has_key(num) and index - nums_dict[num] <= k:
                return True
            nums_dict[num] = index
        return False


sol = Solution()
print sol.containsNearbyDuplicate([1,2,3,4,5,3,4,3],2)        