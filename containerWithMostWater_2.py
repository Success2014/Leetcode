# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:30:40 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxH = 0
        
        while i < j:
            tmp = min(height[i], height[j]) * (j - i)
            if tmp > maxH:
                maxH = tmp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maxH