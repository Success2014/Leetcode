# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 15:22:36 2015

After robbing those houses on that street, the thief has found himself a new 
place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one.
Meanwhile, the security system for these houses remain the 
same as for those in the previous street.

Given a list of non-negative integers representing the amount of 
money of each house, determine the maximum amount of money you can 
rob tonight without alerting the police.


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        """做两次实验。第一次抛开第一家，第二次抛开最后一家，然后看怎样最大。
        原因是最优结果肯定要么在0:n-1这个范围，要么在1:n这个范围产生。
        注意判断一下只有一间房子的情况"""
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        noFirst = self.helper(nums[1:])
        noLast = self.helper(nums[:-1])
        return max(noFirst, noLast)
        
        
    def helper(self,nums):
        size = len(nums)
        odd = 0
        even = 0
        for i in xrange(size):
            if i % 2:
                odd = max(odd + nums[i], even)
            else:
                even = max(even + nums[i], odd)
        return max(odd,even)