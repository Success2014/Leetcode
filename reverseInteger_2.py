# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 21:47:22 2015

@author: Neo
"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        tmp = x
        if x < 0:
            tmp = -tmp
        
        res = 0
        while tmp:
            res = res * 10 + tmp % 10
            tmp /= 10
            
        if (res < -2147483648) or (res > 2147483647): #-2^31, 2^31 -1, 32 bit signed int
            return 0
        
        if x > 0:
            return res
        else:
            return -res
    
    
    def reverse2(self, x):
        """这个也可以AC"""
        tmp = x
        if x < 0:
            tmp = -tmp
        
        res = str(tmp)
        res = int(res[::-1])
        
            
        if (res < -2147483648) or (res > 2147483647): #-2^31, 2^31 -1, 32 bit signed int
            return 0
        
        if x > 0:
            return res
        else:
            return -res


x = -123
sol = Solution()
print sol.reverse2(x)