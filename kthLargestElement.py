# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:50:56 2015

Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

idea:
quick select, not in place, O(n)
random select, in place, O(n)
sort: O(nlogn)

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        """Use a pivot."""
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        p = nums[0] # pivot
        j = 0 # pointer, right of pointer are small numbers, left of pointer are big numbers
        for i in xrange(1, len(nums)):
            if nums[i] > p:
                nums[i], nums[j+1] = nums[j+1], nums[i]
                j += 1
        nums[0], nums[j] = nums[j], nums[0]
                
        if k == j + 1:
            return nums[j]
        elif k > j + 1:
            return self.findKthLargest(nums[j+1:], k - j - 1)
        else:
            return self.findKthLargest(nums[:j], k)
    
    def findKthLargestNIP(self, nums, k):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        p = nums[0] # pivot
        num_s = [] # small numbers
        num_l = [] # large numbers
        for num in nums:
            if num < p:
                num_s.append(num)
            elif num > p:
                num_l.append(num)
        if k <= len(num_l):
            return self.findKthLargestNIP(num_l, k)
        elif k > len(nums) - len(num_s): # wrong if using len(num_l) + 1
            return self.findKthLargestNIP(num_s, k - (len(nums) - len(num_s))) 
            # len(nums) - len(num_s) is the number of digits discarded
        return p
        
        
sol = Solution()        
print sol.findKthLargestNIP([-1,-1],2)
        