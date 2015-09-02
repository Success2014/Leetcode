# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 10:18:21 2015

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Tags: String

idea:
设置一个prev,一个count。
如果当前的数等于prev,那么count + 1, prev不变；
如果当前的数不等prev,那么返回，重置count, prev改为当前值


@author: Neo
"""

def countAndSay(n):
    
    result = list(str(1))#用来更新结果
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