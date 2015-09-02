# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:02:51 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R: # 没有等号的话，a2找不出来
            M = (L + R) / 2
            if nums[M] == target:
                return True
            if nums[L] == nums[M] == nums[R]:
                L += 1
                R -= 1
                
            elif nums[M] >= nums[L]: #左边有序，必须有等号，否则a3通不过
                if nums[M] > target and nums[L] <= target: # target在此区间
                    R = M - 1
                else:#target必不在此区间
                    L = M + 1
            else: # 左边无序，则右边必然有序
                if nums[R] >= target and nums[M] < target: 
                    L = M + 1
                else:#注意舍弃一边的时候，要考虑可能相等num[R]==target
                    R = M -1            
            
        return False