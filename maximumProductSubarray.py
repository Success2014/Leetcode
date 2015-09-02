# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 17:07:22 2015

Find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Tags: Array Dynamic Programming
Similar Problems (M) Maximum Subarray (M) Product of Array Except Self



Example Questions Candidate Might Ask:
Q: Could the subarray be empty?
A: No, the subarray must contain at least one number.

Solution:
This problem is very similar to Question [45. Maximum Sum Subarray]. 
There is a slight twist though. Besides keeping track of the largest product, 
we also need to keep track of the smallest product. Why? The smallest product, 
which is the largest in the negative sense could become the maximum when being 
multiplied by a negative number.
Let us denote that:
f(k) = Largest product subarray, from index 0 up to k.
Similarly,
g(k) = Smallest product subarray, from index 0 up to k.
Then,
f(k) = max( f(k-1) * A[k], A[k], g(k-1) * A[k] )
g(k) = min( g(k-1) * A[k], A[k], f(k-1) * A[k] )
There we have a dynamic programming formula. Using two arrays of size n, we 
could deduce the final answer as f(n-1). Since we only need to access its 
previous elements at each step, two variables are sufficient.

注意maxEndingHere不一定是单增的。
       2  1  -3  2   4  -6 
maxEH  2  2  -3  2   8  288
minEH  2  1  -6 -12 -48 -48
maxSF  2  2   2  2   8  288


@author: Neo
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        maxEningHere = nums[0]
        maxSoFar = nums[0]
        minEningHere = nums[0]
        
        for i in xrange(1, len(nums)):
            maxTnum = maxEningHere*nums[i]
            minTnum = minEningHere*nums[i]
            maxEningHere = max(maxTnum, nums[i], minTnum)
            maxSoFar = max(maxSoFar, maxEningHere)
            minEningHere = min(maxTnum, nums[i], minTnum)
        return maxSoFar
        
sol = Solution()        
print sol.maxProduct([-3,5,3,-6,-4])
        
        
        
        
