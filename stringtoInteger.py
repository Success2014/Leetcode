# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 09:46:34 2015

Caveats:
1. white space
2. sign
3. overflow

@author: Neo
"""

def myAtoi(string):
    if string == "":
        return 0
    
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    n = len(string)
    
    i = 0
    while string[i].isspace() and i < n:
        i += 1
    
    sign = 1
    if i < n and string[i] == "+":        
        i += 1
    elif i < n and string[i] == "-":
        sign = -1
        i += 1

    
    result = 0
    while i < n and string[i].isdigit():
        digit = int(string[i])
    
        if result * 10 > INT_MAX or (result == INT_MAX / 10 and digit >= 8):
            if sign == 1:
                return INT_MAX 
            else:
                return INT_MIN
        else:
            result = result * 10 + digit                        
                
        
        
        i += 1
    
    return sign*result
    
    

a = " +-123"
print myAtoi(a)