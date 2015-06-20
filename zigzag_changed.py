# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 10:46:52 2015

@author: Neo
"""



def convert(s, numRows):
    if numRows <= 1:
        return s
    result = ""
    for i in range(numRows):
        if (i == 0) or i == (numRows -1): # the first and last row
            step = (numRows - 1) + (numRows - 2) + 1            
        else:
            step = numRows - 1
        result += s[i::step]
    return result
        
a = "PAYPALISHIRING"
print "result is :", convert(a, 2)
      
        
        