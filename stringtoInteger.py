# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 09:46:34 2015

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, 
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given 
input specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until 
the first non-whitespace character is found. Then, starting from this character,
 takes an optional initial plus or minus sign followed by as many numerical 
 digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral 
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid 
integral number, or if no such sequence exists because either str is empty or 
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. 
If the correct value is out of the range of representable values, 
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.



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
    
        if result > INT_MAX / 10 or (result == INT_MAX / 10 and digit>=8):
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