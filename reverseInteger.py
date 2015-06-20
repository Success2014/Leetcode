# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 09:00:35 2015

For overflow problem:
n Python integers will automatically switch from a fixed-size int 
representation into a variable width long representation once you pass the 
value sys.maxint, which is either 231 - 1 or 263 - 1 depending on your 
platform. Notice the L that gets appended here.
E.g. 10**30

@author: Neo
"""

def reverse(x):
    if x > 0:
        tmp = x
    else:
        tmp = -x
    
    result = 0
    while tmp != 0:
        result = result * 10 + tmp % 10
        tmp /= 10
        
    if (result < -2147483648) or (result > 2147483647): #-2^31, 2^31 -1, 32 bit signed int
        return 0 # not necessary for python, only need to pass leetcode oj
    
    if x > 0:
        return result
    else:
        return -result


a = -100
print reverse(a)
    
    