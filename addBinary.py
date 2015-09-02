# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 10:23:34 2015

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Tags: Math String
Similar Problems: (M) Add Two Numbers (M) Multiply Strings (E) Plus One (E) Add Binary




idea: from the back, do addition sequentially.
Be careful with the carry.


@author: Neo
"""

def addBinary(a, b):
    
    if len(a) < len(b): # make sure a is longer
        a, b = b, a
    
    m = len(a)
    n = len(b)
    
    result = []
    r = 0 # result bit
    c = 0 # carry bit
    
    for k in xrange(len(a)):
        i = m - 1 - k # from back to front
        
        if k < n: 
            j = n - 1 - k
            r = (int(a[i]) + int(b[j]) + c) % 2
            c = (int(a[i]) + int(b[j]) + c) / 2
        else:
            r = (int(a[i]) + c) % 2
            c = (int(a[i]) + c) / 2
        
        result.insert(0, str(r))
    
    if c == 1:
        result.insert(0, str(c))
    print result
    return ''.join(result)


def addBinary2(a, b):
    list_a = [int(i) for i in a[::-1]]
    list_b = [int(i) for i in b[::-1]]
    
    la = len(list_a)
    lb = len(list_b)
    
    if la < lb:
        list_a += [0 for i in range(lb - la)]
        la = len(list_a)
    else:
        list_b += [0 for i in range(la - lb)]
        lb = len(list_b)
    
    carry = 0
    result = []
    
    for i in range(la):
        t = (list_a[i] + list_b[i] + carry) % 2
        carry = (list_a[i] + list_b[i] + carry) / 2
        result.append(t)
    
    if carry == 1:
        result.append(1)
    
    return ''.join([str(i) for i in result[::-1]])





a = "11"
b = "1"
c = '0'
d = '0'
print addBinary(c,d)
print addBinary2(a,b)
