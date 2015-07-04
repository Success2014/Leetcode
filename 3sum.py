# -*- coding: utf-8 -*-
"""
Created on Sat Jul 04 14:50:28 2015

Given an array S of n integers, are there elements a, b, c in S 
such that a + b + c = 0? Find all unique triplets in the array which 
gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

思路：先sort array, O(nlogn).
然后从左到右看每一个数num[i],找它右边是否有两个数之和为-num[i], O(n2).
注意，重复的不用看了。



@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in xrange(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left - 1] == nums[left]:                        
                            left += 1
                        while left < right and nums[right + 1] == nums[right]:                        
                            right -= 1
                    elif s < 0:
                        left += 1
                    else:
                        right -= 1
        
        return res
                
                
sol = Solution()                
#print sol.threeSum([-1, 0, 1, 2, -1, -4])
print sol.threeSum([0,0,0])                
                
                
                
                
                
                
                
                
                
                
                
                
                