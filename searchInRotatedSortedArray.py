# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:26:19 2015

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, 
otherwise return -1.

You may assume no duplicate exists in the array.

Tags: Array Binary Search
Similar Problems: (M) Search in Rotated Sorted Array II (M) Find Minimum in 
Rotated Sorted Array



@author: Neo
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        
        L = 0
        R = len(nums) - 1
        while L <= R: # 没有等号的话，a2找不出来
            M = (L + R) / 2
            if nums[M] == target:
                return M
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
            
        return -1
        
        
a1 = [4, 5, 6, 7, 0, 1, 2]
a2 = [1]
a3 = [3,1]
sol = Solution()
print sol.search(a1,2)
print sol.search(a2,1)
print sol.search(a2,2)
print sol.search(a3,1)