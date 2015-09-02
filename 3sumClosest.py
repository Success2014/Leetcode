# -*- coding: utf-8 -*-
"""
Created on Sat Jul 04 15:33:41 2015

Given an array S of n integers, find three integers in S such that the sum is 
closest to a given number, target. Return the sum of the three integers. 

You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Idea:
Sort the array.
Use a variable mindf to track the minimum difference.
Use two pointers. If == target, return; > target, right--; < target, left++;

Tags: Array Two Pointers
Similar Problems: (M) 3Sum



@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        mindf = 2147483648
        nums.sort()
        for i in xrange(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                diff = s - target
                if abs(diff) < abs(mindf):
                    mindf = diff
                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1
                    
        return mindf + target

                    
                    
sol = Solution()                    
#print sol.threeSumClosest([-1, 2, 1, -4], 1)
#print sol.threeSumClosest([0,1,2], 0)  
#print sol.threeSumClosest([1,2,4,8,16,32,64,128], 82)                    
print sol.threeSumClosest([0,-1,2], 2)  
                    
                    