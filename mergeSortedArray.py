# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 15:20:37 2015

合并A、B两个有序数组到A中。
从前向后放不行，那就从后向前放吧
Merge from the back to make use of the space.
Put the bigger value at the end.
Don't forget to merge the remaining elements.

@author: Neo
"""

def merge(A, m, B, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]            
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1
    
    

