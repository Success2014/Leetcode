# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:59:26 2015

@author: Neo
"""

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if not str:
            return 0
        n = len(str)
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        i = 0
        
        while i < n and str[i].isspace():
            i += 1
            
        sign = 1
        if i < n and str[i] == "+":
            i += 1
        elif i < n and str[i] == "-":
            sign = -1
            i += 1
            
        res = 0
        
        while i < n and str[i].isdigit():
            digit = int(str[i])
            if res > INT_MAX/10 or (res == INT_MAX / 10 and digit>=8):
                if sign > 0:
                    return INT_MAX
                else:
                    return INT_MIN
            res = res * 10 + digit
            i += 1
        
        return sign*res 
        
        
        
        
            
sol = Solution()
print sol.myAtoi("+123")
print sol.myAtoi("      -11919730356x")