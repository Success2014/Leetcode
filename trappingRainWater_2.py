# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:15:52 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height:
            return 0
            
        maxSoFar = 0
        maxToLeft = []
        for h in height:
            if h > maxSoFar:
                maxSoFar = h
            maxToLeft.append(maxSoFar)
        
        maxSoFar = 0
        maxToRight = []
        for h in height[::-1]:
            if h > maxSoFar:
                maxSoFar = h
            maxToRight.insert(0,maxSoFar)
        
        count = 0
        for i in xrange(len(height)):
            t = min(maxToLeft[i],maxToRight[i]) 
            count += max(t - height[i],0)
        
        return count
            
            
            
        
        
            
            
            
        
        