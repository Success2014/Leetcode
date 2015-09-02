# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:32:24 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        if not s:
            return False
        n = len(s)
        i = 0
        while i < n and s[i].isspace():#space
            i += 1
        
        Flag = False
        
        if i < n and (s[i] == "+" or s[i] == "-"):#sign
            i += 1
        
        while i < n and s[i].isdigit():#digits
            i += 1
            Flag = True
        
        if i < n and s[i] == ".":#decimal point, no change
            i += 1
            
        while i < n and s[i].isdigit():#可以放在上面if循环内
            i += 1
            Flag = True
        
        if i < n and Flag and (s[i] == "e" or s[i] == "E"):#expon
            i += 1
            Flag = False
            
            if i < n and (s[i] == "+" or s[i] == "-"):
                i += 1
        
            while i < n and s[i].isdigit():
                i += 1
                Flag = True
        
        while i < n and s[i].isspace():#space
            i += 1
        
        return Flag and (i==n)
        
        
        
        
        
            
            
    