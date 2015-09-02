# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 09:31:39 2015

Input is guaranteed to be within the range from 1 to 3999.
Avoid four symbols being repeated in succession.

Tags: Math String
Similar Problems (E) Roman to Integer

idea:
See handbook.

additive notation:
subtractive notation: Four characters are avoided being repeated in succession.

@author: Neo
"""

def intToRoman(num):
    values = [1000, 900, 500, 400, 
              100, 90, 50, 40,
              10, 9 , 5, 4,
              1]
    symbols = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV",
               "I"]
    result = ""
    while num > 0:
        for i, val in enumerate(values):
            div = num / val
            for j in range(div):
                result += symbols[i]
                num -= val
                
    return result
    

print intToRoman(4)
    