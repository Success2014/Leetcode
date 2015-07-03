# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 17:40:21 2015

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.

You may assume no duplicate exists in the array.


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        """思路参考handbook"""
        
        L = 0
        R = len(nums) - 1
        while (L < R): # solution 上有 and (A[L] > A[R])
            M = (L + R)/2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]
    
    

sol = Solution()    
print sol.findMin([6,7,1,2,3,4,5])
print sol.findMin([4,5,6,7,1,2,3])