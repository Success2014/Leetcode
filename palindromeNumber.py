# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 11:15:07 2015

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

@author: Neo
"""

def isPalindrome(x):
    if x < 0:
        return False
    
    div = 1
    while x/div > 0:
        div *= 10
    
    div /= 10
    
    while x != 0:
        head = x / div
        tail = x % 10
        if head != tail:
            return False
        x = (x % div) / 10
        div /= 100
    
    return True
    

print isPalindrome(5214125)    