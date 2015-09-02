# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 17:58:11 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        pivot = nums[0]
        j = 0
        for i in xrange(1,len(nums)):
            if nums[i] > pivot:
                nums[j+1],nums[i] = nums[i],nums[j+1]
                j += 1
        nums[0], nums[j] = nums[j],nums[0]
        
        if k == j + 1:
            return nums[j]
        elif k > j + 1:
            return self.findKthLargest(nums[j+1:],k-j-1)
        else:
            return self.findKthLargest(nums[:j],k)
            
        
sol = Solution()        
nums = [-1,2,0]
k = 1
print sol.findKthLargest(nums,k)