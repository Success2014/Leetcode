# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 11:35:25 2015

idea: if the digit is 0-8, it is straightforward; if
the digit is 9, need to take care of the carry

@author: Neo
"""

def plusOne(digits):
    result = []
    digits.reverse()
    
    carry = 0    
    
    t = (digits[0] + 1 + carry) % 10
    carry = (digits[0] + 1 + carry) / 10
    result.append(t)
    
    for d in digits[1:]:
        t = (d + carry) % 10
        carry = (d + carry) / 10
        result.append(t)
    if carry == 1:
        result.append(1)
    
    result.reverse()
    return result
        
        
digits = [1,9,9]
print plusOne(digits)
    