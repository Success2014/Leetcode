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


Tags: Array Greedy


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        """每一步都看前面最多还可以走多少步。greedy.还有步子走的话，就一直走
        下去，直到终点。"""
        step = nums[0]
        for i in xrange(1,len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True
    def canJump2(self, nums):
        """比如nums=[1,2,3],看每个entry的时候，看他能走多远。最后一个不看。
        所以，这个数组可以走到0+1=1 和1+2=3。最大的3>2，所以是可以到末尾的。
        但是这样看有个问题比如nums=[0,2,3],上面的做法算出来就是[0,3],3>2.
        但是实际上市到达不了的。所以要增加一个判断是否能到达当前这一步。"""
        max = 0
        
        for i in xrange(len(nums)-1):
            if (i + nums[i]) > max and max >= i:
                max = i + nums[i]
        
        if max >= len(nums) - 1:
            return True
        else:
            return False


sol = Solution()        
print sol.canJump([2,3,1,1,4])
print sol.canJump([3,2,1,0,4])