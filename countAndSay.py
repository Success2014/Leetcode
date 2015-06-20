# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 10:18:21 2015



@author: Neo
"""

def countAndSay(n):
    
    result = list(str(1))
    for i in xrange(1,n):
        tmp = []
        prev = None
        count = 1
        for s in result:
            if s == prev:
                count += 1
            if (prev is not None) and s != prev:
                tmp.append(str(count))
                tmp.append(str(prev))                
                count = 1
            prev = s
        tmp.append(str(count))
        tmp.append(str(prev))
        result = tmp
    return ''.join(result)
    


print countAndSay(6)    