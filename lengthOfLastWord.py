# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 13:10:28 2015

@author: Neo
"""

def lengthOfLastWord(s):
    
    if s.split() == []:
        return 0
    else:
        return len(s.split()[len(s.split()) - 1])
        
def lengthOfLastWord2(s):
    
    n = len(s)
    if n == 0:
        return 0
    i = n - 1 # last position of non-white-space
    while (i >= 0) and (s[i] == " ") :
        i -= 1
    
    j = i - 1 # position of last white space
    while (j >= 0) and (s[j] != " "):
        j -= 1
        
    return i - j if i >= 0 else 0


s1 = "a"    
s2 = " "
print lengthOfLastWord2(s1)
print lengthOfLastWord(s2)