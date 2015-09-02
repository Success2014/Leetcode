# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 16:42:59 2015

Find the contiguous subarray within an array (containing at least one number) 
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using 
the divide and conquer approach, which is more subtle.

Dynamic Programming:
O(n) runtime, O(1) space – Dynamic programming:
To devise a dynamic programming formula, let us assume that we are calculating 
the maximum sum of subarray that ends at a specific index.
Let us denote that:
f(k) = Maximum sum of subarray ending at index k.
Then,
f(k) = max( f(k-1) + A[k], A[k] )
Using an array of size n, We could deduce the final answer by as f(n – 1), with
the initial state of f(0) = A[0]. Since we only need to access its previous 
element at each step, two variables are sufficient. Notice the difference 
between the two: maxEndingHere and maxSoFar; the former is the maximum sum of 
subarray that must end at index k, while the latter is the global maximum 
subarray sum.


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        maxEndingHere = nums[0]
        maxSoFar = nums[0]
        
        for i in xrange(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i]) 
            #要么以当前这个数开始，要么加上这个数
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar


sol = Solution()        
print sol.maxSubArray([-3,8,3,-2,-4])