# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 14:56:20 2015

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
        lowerleft_x = max(A,E)
        lowerleft_y = max(B,F)
        upperright_x = min(C,G)
        upperright_y = min(D,H)
        
        if upperright_x > lowerleft_x and upperright_y > lowerleft_y:
            return (C-A)*(D-B)+(G-E)*(H-F)-(upperright_x-lowerleft_x)*(upperright_y-lowerleft_y)
        else:#没有交点
            return (C-A)*(D-B)+(G-E)*(H-F)