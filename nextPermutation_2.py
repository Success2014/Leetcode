# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 19:55:45 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n = len(nums)
        if n > 1:
            i = n - 1
            p = -1
            t = 0
            while i >= 1:
                if nums[i-1] < nums[i]:
                    p = i - 1 # index to 
                    break
                i -= 1
            if p >= 0:
                i = n - 1
                while i >= 0:
                    if nums[i] > nums[p]:
                        t = i
                        break
                    i -= 1
                
                nums[p], nums[t] = nums[t], nums[p]
            
            nums = nums[0:p+1] + nums[p+1:][::-1]#OJ不能AC,但应该是对的
        
        return nums
            
                
            
            
sol = Solution()                
print sol.nextPermutation([1,3,2])
print sol.nextPermutation([2,3,1])
print sol.nextPermutation([3,2,1])