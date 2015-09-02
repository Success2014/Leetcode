# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 11:21:54 2015

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
 rows like this: (you may want to display this pattern in a fixed font for 
 better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number 
of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

注意比如4行的时候会是：
P     I
A   L
Y A
P

idea:两个指针，ind_tmp指向第几行, ind是字符串的指针
2个corner cases:到最下面之后掉头，到最上面之后掉头
@author: Neo
"""

def convert(s, numRows):
    """第2次的写法更好"""
    if numRows == 1:
        return s
    
    tmp = ["" for i in range(numRows)]     
    ind_tmp = -1 # which element of tmp will take the new value
    direction = 1 # 1: forward, -1: backward
    for ind, val in enumerate(s):
        if ind_tmp == numRows - 1:
            direction = -1
        ind_tmp += direction
        if ind_tmp == -1:
            ind_tmp = 1
            direction = 1
        tmp[ind_tmp] += val
    return ''.join(tmp)

def convert2(self, s, numRows):
        if numRows == 1:
            return s
        
        tmp = ["" for i in xrange(numRows)]
        direction = 1
        idx = -1
        for i in xrange(len(s)):
            idx += direction
            tmp[idx] += s[i]
            if idx == numRows - 1:
                direction = -1
            elif idx == 0:
                direction = 1
        
        return ''.join(tmp)    

def convert3(s, numRows):
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
print "result is :", convert(a, 3)
      