# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 16:05:07 2015

Given a sorted array of integers, find the starting and ending position of a 
given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].


idea:
define two helper functions: findLeft, findRight.
1 2 2 2 3

How to handle the case when A[mid] = target?
findLeft all the way to the left until left > right,
findRight all the way to the right until left > right.


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        left = self.findLeft(nums,target)
        right = self.findRight(nums,target)
        return [left, right]
        
    def findLeft(self, nums, target):
        n = len(nums)
        L = 0
        R = n - 1
        while L <= R:
            M = (L+R) / 2
            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else: #nums[M] = target
                R = M - 1
        if L < n and nums[L] == target:
            return L
        return -1
        
    def findRight(self, nums, target):
        n = len(nums)
        L = 0
        R = n - 1
        while L <= R:
            M = (L+R) / 2
            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else: #nums[M] = target
                L = M + 1
        if R < n and nums[R] == target:
            return R
        return -1
        
        
        
sol = Solution()
print sol.searchRange([1,2,2,2,3],2)

        
        
        
        