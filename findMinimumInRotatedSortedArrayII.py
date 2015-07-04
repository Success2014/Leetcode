# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 19:37:59 2015


Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
The array may contain duplicates.

solution:

For case where AL == AM == AR, the minimum could be on AM’s left or right side (eg,
[1, 1, 1, 0, 1] or [1, 0, 1, 1, 1]). In this case, we could not discard either subarrays and
therefore such worst case degenerates to the order of O(n).
不会出现[0,0,0,1,0]，因为不是sorted array

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        L = 0
        R = len(nums) - 1
        while (L < R) and (nums[L] >= nums[R]): # 没有and后面处理不了两个数的情况,e.g.[1,3]        
            M = (L + R)/2
            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[L]:
                R = M
            else: # nums[L] = nums[M] = nums[R]
                L += 1
        return nums[L]

sol = Solution()    
print sol.findMin([6,7,1,2,3,4,5])
print sol.findMin([4,5,6,7,1,2,3])
print sol.findMin([1,3])        
print sol.findMin([1, 1, 1, 0, 1]) # while判定没有等号的话，这个会出错