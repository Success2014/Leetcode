# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 16:30:46 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
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