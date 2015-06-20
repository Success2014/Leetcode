# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 10:24:46 2015

idea: scan it brutally

@author: Neo
"""

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
        
    if len(strs) == 1:
        return strs[0]
    
    tmp = strs[0] # use the first string as the benchmark
    
    result = ''
    for i in xrange(len(tmp)):
        for s in strs[1:]:
            if i == len(s) or s[i] != tmp[i]: # if longer than or not equal
                return result
        result += tmp[i]
    return result
    
    
strs = ['aa', 'a']
print longestCommonPrefix(strs)
        
    
    