# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 15:55:52 2015

Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.

解题思路：不许用乘、除和求余实现两数的相除。那就只能用加和减了。
正常思路是被除数一个一个的减除数，直到剩下的数比除数小为止，就得到了结果。
这样是无法ac的，因为时间复杂度为O(n)，比如一个很大的数除1，就很慢。
这里我们可以用二分查找的思路，可以说又是二分查找的变种。

比如84除以4
第一轮84
sum:   4 8 16 32 64
count: 1 2 4  8  16
第二轮84-64=20
sum:   4 8 16
count: 1 2 4
第三轮84-64-16=4
sum:  4
count: 1
所以结果是16+4+1=21


注意不能用乘法，除法和取模。

注意python是向下取整 -1/2=-1而不是0

@author: Neo
"""

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        
        res = 0
        
        dd = abs(dividend)
        dr = abs(divisor)
                
        while dd >= dr:
            s = dr
            c = 1
            
            while s + s <= dd:
                s += s
                c += c
            res += c
            dd -= s
        
         
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            if res >= 2147483648: # if overflows
                return 2147483647
            return res
        else:
            if res >= 2147483648: # if overflows
                return -2147483648
            return 0 - res

sol = Solution()
print sol.divide(-16,3)
print sol.divide(-84,4)
print sol.divide(1,1)
print sol.divide(1,-1)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        