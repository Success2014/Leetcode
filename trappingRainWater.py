# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:55:44 2015

Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!

Tags: Array Stack Two Pointers
Similar Problems: (M) Container With Most Water 
(M) Product of Array Except Self


idea:
用leftMostHigh[i]来记录从左到右到i这个位置左边最高峰，
用rightMostHigh[i]来记录从右到左到i这个位置右边最高峰。
然后i这个位置能装的水就是二者中小的一个减去height[i].

原理就是：想象一个大坝，先修好了最左边的堤和最右边的堤，然后中间就可以装水了。
但是如果中间有石头的话，就要减去石头的容量。
但是中间的石头，也许可以护起更高的水位。

画出下面的水位秒懂
[1, 0, 2, 1, 0, 2] height
    1     1  2
 1, 1, 2, 2, 2, 2  left
 2, 2, 2, 2, 2, 2  right

[1, 0, 0, 2, 0, 0, 2] height
    1  1     2  2
 1, 1, 1, 2, 2, 2, 2  left
 2, 2, 2, 2, 2, 2, 2  right




@author: Neo
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        leftMax = 0
        leftMost = [0 for i in range(n)]
        rightMax = 0
        rightMost = [0 for i in range(n)]
        
        total = 0
        
        for i in xrange(n):
            if height[i] > leftMax:
                leftMax = height[i]
            leftMost[i] = leftMax
        
        for j in xrange(n-1, -1, -1):
            if height[j] > rightMax:
                rightMax = height[j]
            rightMost[j] = rightMax
            
            total += min(leftMost[j],rightMost[j]) - height[j]
        
        return total


height1 = [1, 0, 2, 1, 0, 2]       
height2 = [1, 0, 0, 2, 0, 0, 2]
        
sol = Solution()
print sol.trap(height1)
print sol.trap(height2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        