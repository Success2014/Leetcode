# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:27:23 2015

Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different 
ways to solve this problem.
Do not return anything, modify nums in-place instead.

Hint:
Could you do it in-place with O(1) extra space?

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate1(self, nums, k): # O(k*n) in time, extra space O(1)
        if not nums:
            return None
        k = k % len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        return nums
    
    def rotate2(self, nums, k): # O(n) in time, extra space O(n)
        if not nums:
            return None
        k = k % len(nums)        
#        nums = nums[-k:] + nums[0:-k] # will fail since new nums created
        nums[:] = nums[-k:] + nums[0:-k]
        return nums
        
    """
    idea: for each number find its togo position, then find the togo position
    for the number replaced.
    
    If len(nums) is divisible by k, it will cycle.
    
    This solution is wrong.
    """
    def rotate3(self, nums, k): 
        if not nums:
            return None
        nums_len = len(nums)
        
        if k < 1 or nums_len <= 1:
            return nums
            
        k = k % nums_len
        
        if nums_len % k == 0:
            tmp1 = nums[-k:]
            for i in xrange(0, nums_len, k):
                tmp2 = nums[i:i + k]
                nums[i: i + k] = tmp1
                tmp1 = tmp2
            return nums
        else:
            index_cur = 0
            tmp1 = nums[index_cur]
            for i in xrange(nums_len):            
                index_togo = (index_cur + k) % nums_len
                tmp2 = nums[index_togo]
                nums[index_togo] = tmp1
                
                index_cur = index_togo
                tmp1 = tmp2
            return nums


sol = Solution()
print sol.rotate3([1,2,3,4,5,6],4)







