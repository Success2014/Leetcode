# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:59:21 2015

Given a sorted array and a target value, return the index if the target is 
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0



@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    """
    A good thing to verify your above binary search does not stuck in an 
    infinite loop is to test with input containing two elements, 
    e.g., [1,3] and test with target = 0 and 1.
    """
    def searchInsert(self, nums, target):
        L = 0 # lowest inclusive index to search
        R = len(nums) - 1 # highest inclusive index to search
        
        while L < R: # when while loop exits, L must be equal to R
            M = (L + R) / 2 # Middle, must be the lower end
            if nums[M] < target:
                L = M + 1
            else:
                R = M 
                
        if nums[L] < target:
            return L + 1
        else:
            return L
    def searchInsert2(self, nums, target):
        """iterative的另一种实现。观察几个例子想出来的。"""
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        return L
            
    
    def searchInsertRec(self, nums, target):
        """recursive"""
        L = 0
        R = len(nums) - 1
        return self.search(nums, target, L, R)
        
    def search(self, nums, target, L, R):
        if L == R:
            if nums[L] >= target:
                return L
            else:
                return L + 1
        M = (L + R) /2
        if nums[M] == target:
            return M
        elif nums[M] < target:
            return self.search(nums, target, M + 1, R)
        else:
            return self.search(nums, target, L, M)
                
sol = Solution()
print sol.searchInsert2([1,3,5],0)
                