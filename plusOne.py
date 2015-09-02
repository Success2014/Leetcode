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


def plusOne2(digits):
    """不需要carry这个东西。如果当前数小于9则加1返回；否则当前位置0，前一位继续加1。
    到第一位都没有返回的话，说明是99..9这样序列，再加一个1"""
    for i in xrange(len(digits)-1, -1, -1):
        d = digits[i]
        if d < 9:
            digits[i] = d + 1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)
    return digits #如果直接return digits.insert(0,1)会出错
        
        
        
#digits = [1,9,9]
#print plusOne2(digits)
digits =[9,9,9]
print plusOne2(digits)
    