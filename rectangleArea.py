# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:45:54 2015
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner 
as shown in the figure.

Assume that the total area is never beyond the maximum possible value of int.

idea:
draw a picture with these points

@author: Neo
"""

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if C < E or G < A or D < F or H < B:
            return (C-A)*(D-B)+(G-E)*(H-F)
                
#        if A == C or B == D: # no need
#            return (G-E)*(H-F)
        
        lowerleft_x = max(A, E)
        lowerleft_y = max(B, F)
        upperright_x = min(C, G)
        upperright_y = min(D, H)
        
        return (C-A)*(D-B)+(G-E)*(H-F) - (upperright_x-lowerleft_x)*(upperright_y-lowerleft_y)
    
    def computeArea2(self, A, B, C, D, E, F, G, H):
        lowerleft_x = max(A, E)
        lowerleft_y = max(B, F)
        upperright_x = min(C, G)
        upperright_y = min(D, H)
        
        return (C-A)*(D-B)+(G-E)*(H-F) - \
        (upperright_x-lowerleft_x)*(upperright_y-lowerleft_y) \
        if upperright_x>lowerleft_x and upperright_y>lowerleft_y \
        else(C-A)*(D-B)+(G-E)*(H-F)
       
       
sol = Solution()            
print sol.computeArea2(0, 0, 0, 0, -1, -1, 1, 1)
            
            
            
            
            
            
            