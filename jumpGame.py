# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 00:13:12 2015

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

idea:
每一步都看前面最多还可以走多少步。greedy.

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        step = nums[0]
        for i in xrange(1,len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True


sol = Solution()        
print sol.canJump([2,3,1,1,4])
print sol.canJump([3,2,1,0,4])