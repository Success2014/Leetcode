# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:14:18 2015

Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Possible solutions:
https://leetcode.com/discuss/37219/possible-solutions

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        nums_dict = {}
        for num in nums:
            if nums_dict.has_key(num):
                return True
            nums_dict[num] = 1
        return False
    def containsDuplicate2(self, nums):
        return len(set(nums)) < len(nums)

sol = Solution()
print sol.containsDuplicate2([1,2,3,1])        