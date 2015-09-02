# -*- coding: utf-8 -*-
"""
Created on Sat Jul 04 14:34:54 2015
Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of 
line i is at (i, ai) and (i, 0). Find two lines, which together 
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
Tags: Array Two Pointers
Similar Problems: (H) Trapping Rain Water


@author: Neo
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        """Use two pointers move from both ends to center.
        Move the pointer with lower height to the other one.
        Stop when two pointers are next to each other."""
        if len(height) < 2:
            return 0
        L = 0
        R = len(height) - 1
        maxarea = 0
        while L < R:
            if height[L] < height[R]:
                maxarea = max(maxarea, height[L] * (R - L))
                L += 1
            else:
                maxarea = max(maxarea, height[R] * (R - L))
                R -= 1
        return maxarea


sol = Solution()            
print sol.maxArea([2,1,5,4])