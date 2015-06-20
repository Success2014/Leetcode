# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 09:12:58 2015

Input is guaranteed to be within the range from 1 to 3999.

idea: if the previous letter is bigger than the current one, just add this one;
otherwise, need to subtract twice the previous one.

@author: Neo
"""

def romanToInt(s):
    roman_dict = {'I' : 1,
                  'V' : 5,
                  'X' : 10,
                  'L' : 50,
                  'C' : 100,
                  'D' : 500,
                  'M' : 1000}
    
    prev = 0
    curr = 0                  
    result = 0
    for letter in s:
        curr = roman_dict.get(letter)
        if curr > prev:
            result += curr - 2 * prev
        else:
            result += curr 
        prev = curr
    return result


print romanToInt('MXCVI')        