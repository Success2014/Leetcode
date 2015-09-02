# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 10:15:53 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry = 0
        for i in xrange(len(digits)-1,-1,-1):
            if i == len(digits) - 1:
                tmp = digits[i]
                carry = (tmp + 1) / 10
                digits[i] = (tmp + 1) % 10
                
            else:
                tmp = digits[i]                
                digits[i] = (tmp + carry) % 10
                carry = (tmp + carry) / 10
                
        if carry == 1:
            digits.insert(0,1)
        return digits
    def plusOne2(self, digits):
        
        for i in xrange(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        digits.insert(0,1)
        return digits
            
            
            
digits1=[3,9]            
sol = Solution()
print sol.plusOne(digits1)